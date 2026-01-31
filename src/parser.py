import re
from typing import List, Optional
from src.models import Resume, Section

class ResumeParser:
    """
    Parses raw text into a structured Resume object.
    """

    def parse(self, text: str) -> Optional[Resume]:
        """
        Parses the complete resume text.

        Args:
            text (str): The raw text content of the resume.

        Returns:
            Resume: A populated Resume object, or None if parsing fails.
        """
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        
        if not lines:
            return None

        resume = Resume()
        
        # 1. Extract Name (First line)
        resume.name = lines[0]
        
        # 2. Extract Contact Info & Sections
        self._extract_sections(lines[1:], resume)
        
        return resume

    def _extract_sections(self, lines: List[str], resume: Resume) -> None:
        """
        Internal method to separate contacts from sections.
        """
        current_section_title = None
        section_buffer = []
        
        for i, line in enumerate(lines):
            if self._is_header(line):
                # Save previous section
                if current_section_title:
                    content_html = self._format_content(section_buffer)
                    resume.sections.append(Section(title=current_section_title, content=content_html))
                    section_buffer = []
                
                # If no section yet, previous lines were contacts
                if current_section_title is None:
                    raw_contacts = lines[:i]
                    self._parse_contacts(raw_contacts, resume)
                
                current_section_title = line
            else:
                if current_section_title:
                    section_buffer.append(line)
                else:
                    # Still in potential contact area, wait for first header
                    pass

        # Append final section
        if current_section_title:
            content_html = self._format_content(section_buffer)
            resume.sections.append(Section(title=current_section_title, content=content_html))
        # Fallback: if no headers found, everything might be contacts (unlikely but possible)
        elif not resume.contacts:
             self._parse_contacts(lines, resume)

    def _is_header(self, line: str) -> bool:
        """
        Determines if a line is likely a section header.
        """
        # Criteria: All Uppercase, reasonable length, specific keywords help
        if not line.isupper():
            return False
        
        if len(line) > 50:
            return False
            
        if '|' in line: # Headers usually don't have separators like this
            return False

        keywords = ['OBJETIVO', 'RESUMO', 'FORMAÇÃO', 'EXPERIÊNCIA', 'HABILIDADES', 'PROJETOS', 'INFORMAÇÕES', 'IDIOMAS', 'EDUCAÇÃO']
        if any(k in line for k in keywords):
            return True
            
        # Generic uppercase line is likely a header if short
        return True

    def _parse_contacts(self, lines: List[str], resume: Resume) -> None:
        """
        Parses contact lines, splitting by pipes if necessary.
        """
        for line in lines:
            parts = [p.strip() for p in line.split('|')]
            resume.contacts.extend(parts)

    def _format_content(self, lines: List[str]) -> str:
        """
        Formats text lines into HTML (lists, paragraphs).
        """
        if not lines:
            return ""
        
        html_parts = []
        in_list = False
        
        for line in lines:
            is_list_item = line.startswith('- ') or line.startswith('• ') or line.startswith('* ')
            is_labeled_item = ':' in line and len(line.split(':')[0]) < 40 and not is_list_item
            
            if is_list_item:
                if not in_list:
                    html_parts.append('<ul>')
                    in_list = True
                clean_line = re.sub(r'^[-•*]\s+', '', line)
                html_parts.append(f'<li>{clean_line}</li>')
            
            elif is_labeled_item:
                 if in_list:
                     html_parts.append('</ul>')
                     in_list = False
                 
                 label, content = line.split(':', 1)
                 html_parts.append(f'<p><strong>{label}:</strong>{content}</p>')
            
            else:
                if in_list:
                    html_parts.append('</ul>')
                    in_list = False
                html_parts.append(f'<p>{line}</p>')
                
        if in_list:
            html_parts.append('</ul>')
            
        return "".join(html_parts)
