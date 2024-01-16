import time

from agency.spaces.local_space import LocalSpace
from agency.agent import Agent, action
from agents.host import Host

if __name__ == "__main__":

    space = LocalSpace()
    other_agent = space.add_foreground(Agent, "ForegroundAgent")
    space.add(Host, "Host")

    other_agent.send({
        "to": "Host",
        "action": {
            "name": "add",
            "args": {
                "a": 1
            }
        },
    })