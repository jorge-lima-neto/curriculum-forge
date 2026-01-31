import os
from jinja2 import Environment, FileSystemLoader
from src.models import Resume

class HTMLGenerator:
    """
    Handles the generation of HTML based on Resume data.
    """
    
    def __init__(self, template_dir: str = 'templates', template_name: str = 'resume.html'):
        """
        Initialize the generator with template settings.
        
        Args:
            template_dir (str): Relative path to the templates directory.
            template_name (str): The name of the Jinja2 template file.
        """
        self.project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.template_path = os.path.join(self.project_root, template_dir)
        self.template_name = template_name
        
        self.env = Environment(loader=FileSystemLoader(self.template_path))
        self.template = self.env.get_template(self.template_name)

    def generate(self, resume: Resume, output_path: str) -> str:
        """
        Generates the HTML file.

        Args:
            resume (Resume): The resume object to render.
            output_path (str): The desired path for the output file.

        Returns:
            str: Absolute path to the generated file.
        """
        html_content = self.template.render(
            name=resume.name,
            contacts=resume.contacts,
            sections=resume.sections
        )
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        return os.path.abspath(output_path)
