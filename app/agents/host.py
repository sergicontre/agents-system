from agency.agent import ACCESS_REQUESTED, Agent, action

class Host(Agent):
    """
    Represents the host system of the running application
    """
    def before_action(self, message: dict):
        """Called before an action is attempted"""
        print("I'm about to do something!")

    def after_action(self, message: dict, return_value: str, error: str):
        """Called after an action is attempted"""
        print("I'm done!", message, error)

    def after_add(self):
        """Called after the agent is added to a space and may begin communicating"""
        print("I'm being added!")

    def before_remove(self):
        """Called before the agent is removed from the space"""
        print("I'm being removed!")

    @action
    def add(self, content: str):
        print("Action executed in agent", content)