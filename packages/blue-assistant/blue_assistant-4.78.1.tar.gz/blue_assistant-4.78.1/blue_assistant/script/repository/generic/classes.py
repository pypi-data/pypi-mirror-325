from typing import Dict, List
import os
from tqdm import tqdm


from blueness import module
from blue_objects import file, path
from blue_objects.metadata import post_to_object

from blue_assistant import NAME
from blue_assistant.script.repository.base.classes import BaseScript
from blue_assistant.script.actions.functions import perform_action
from blue_assistant.logger import logger


NAME = module.name(__file__, NAME)


class GenericScript(BaseScript):
    name = path.name(file.path(__file__))

    def run(
        self,
    ) -> bool:
        if not super().run():
            return False

        success: bool = True
        while not all(self.nodes[node]["completed"] for node in self.nodes) and success:
            for node_name in tqdm(self.nodes):
                if self.nodes[node_name]["completed"]:
                    continue

                pending_dependencies = [
                    node_name_
                    for node_name_ in self.G.successors(node_name)
                    if not self.nodes[node_name_]["completed"]
                ]
                if pending_dependencies:
                    logger.info(
                        'node "{}": {} pending dependenci(es): {}'.format(
                            node_name,
                            len(pending_dependencies),
                            ", ".join(pending_dependencies),
                        )
                    )
                    continue

                if not perform_action(
                    script=self,
                    node_name=node_name,
                ):
                    success = False
                    break

                self.nodes[node_name]["completed"] = True

        if not post_to_object(
            self.object_name,
            "output",
            self.metadata,
        ):
            return False

        return success
