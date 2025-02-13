import re


class PromptLang:
    def __init__(self, data, cache):
        self.data = data
        self.cache = cache

    def get_nested_value(self, key):
        """Safely fetch a nested value from a dictionary using dot notation."""
        keys = key.split(".")
        value = self.data
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return None  # Key not found
        return value

    def evaluate_expression(self, expression, is_mandatory):
        """Evaluates an expression, ensuring mandatory fields exist before function calls."""
        
        if expression.startswith("fn:"):
            func_match = re.match(r"fn:(\w+)\s*(.*)", expression)
            if func_match:
                func_name, args = func_match.groups()
                func = globals().get(func_name)  # Fetch function from helper_function.py
                
                arg_values = [self.get_nested_value(arg) for arg in args.split() if arg]
                
                if is_mandatory and (not arg_values or any(v is None or str(v).strip() == "" for v in arg_values)):
                    return f"MISSING: {args.strip()}"

                cache_key = f"{func_name}:{','.join(map(str, arg_values))}"
                if cache_key in self.cache:
                    return self.cache[cache_key]

                result = func(*arg_values) if func and arg_values else None
                self.cache[cache_key] = result
                return result
        
        else:
            value = self.get_nested_value(expression)
            if is_mandatory and (value is None or str(value).strip() == ""):
                return f"MISSING: {expression}"
            return value

    def process_placeholder(self, match):
        expression = match.group(1).strip()
        is_mandatory = expression.startswith("mandatory ")

        if is_mandatory:
            expression = expression.replace("mandatory ", "", 1).strip()

        if "|" in expression:
            parts = [part.strip() for part in expression.split("|")]
            for part in parts:
                value = self.evaluate_expression(part, is_mandatory)
                if value and not str(value).startswith("MISSING:"):
                    return str(value)
            return f"MISSING: {expression}" if is_mandatory else ""

        value = self.evaluate_expression(expression, is_mandatory)
        if is_mandatory and str(value).startswith("MISSING:"):
            return value
        return str(value) if value else ""

    def generate_prompt(self, template):
        placeholders = re.findall(r"{(.*?)}", template)
        for placeholder in placeholders:
            processed_value = self.process_placeholder(re.match(r"{(.*?)}", f"{{{placeholder}}}"))
            if processed_value.startswith("MISSING:"):
                return processed_value
        
        return re.sub(r"{(.*?)}", lambda match: self.process_placeholder(match), template)


