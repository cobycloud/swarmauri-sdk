from abc import ABC, abstractmethod
from typing import Dict

class ITemplate(ABC):
    """
    Interface for template-based prompt generation within the SwarmAURI framework.
    Defines standard operations and attributes for managing and utilizing templates.
    """

    @property
    @abstractmethod
    def template(self) -> str:
        """
        Abstract property to get the current template string.
        """
        pass

    @template.setter
    @abstractmethod
    def template(self, value: str) -> None:
        """
        Abstract property setter to set or update the current template string.

        Args:
            value (str): The new template string to be used for generating prompts.
        """
        pass


    @property
    @abstractmethod
    def variables(self) -> List[Dict[str, str]]:
        """
        Abstract property to get the current set of variables for the template.
        """
        pass

    @variables.setter
    @abstractmethod
    def variables(self, value: List[Dict[str, str]]) -> None:
        """
        Abstract property setter to set or update the variables for the template.
        """
        pass

    @abstractmethod
    def set_template(self, template: str) -> None:
        """
        Sets or updates the current template string.

        Args:
            template (str): The new template string to be used for generating prompts.
        """
        pass

    @abstractmethod
    def set_variables(self, variables: List[Dict[str, str]]) -> None:
        """
        Sets or updates the variables to be substituted into the template.

        Args:
            variables (List[Dict[str, str]]): A dictionary of variables where each key-value 
                                        pair corresponds to a placeholder name and its 
                                        replacement value in the template.
        """
        pass

    @abstractmethod
    def generate_prompt(self, **kwargs) -> str:
        """
        Generates a prompt string based on the current template and provided keyword arguments.

        Args:
            **kwargs: Keyword arguments containing variables for template substitution. 

        Returns:
            str: The generated prompt string with template variables replaced by their
                 corresponding values provided in `kwargs`.
        """
        pass