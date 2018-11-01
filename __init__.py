# show me the way.

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = '66president'

LOGGER = getLogger(__name__)


class pathguideSkill(MycroftSkill):
    def __init__(self):
        super(pathguideSkill, self).__init__(name="pathguideSkill")

    def initialize(self):
        show_me_the_way_to_office_room_intent = IntentBuilder("ShowMetheWayToOfficeroomIntent"). \
            require("ShowMetheWaytoOfficeroomKeyword").build()
        self.register_intent(show_me_the_way_to_office_room_intent, 
                             self.handle_show_me_the_way_to_office_room_intent)

        show_me_the_way_to_science_fair_intent = IntentBuilder("ShowMetheWayToToiletIntent"). \
            require("ShowMetheWayToToiletKeyword").build()
        self.register_intent(show_me_the_way_to_science_fair,
                             self.handle_show_me_the_way_to_science_fair_intent)

        show_me_the_way_to_principal_room_intent = IntentBuilder("ShowMetheWayToPrincipalroomIntent"). \
            require("ShowMetheWayToPrincipalroomKeyword").build()
        self.register_intent(show_me_the_way_to_principal_room_intent,
                             self.handle_show_me_the_way_to_principal_room_intent)

    def handle_show_me_the_way_to_officeroom_intent(self, message):
        self.speak_dialog("office.room.is.4th.room.from.left.to.right.at.groundfloor")

    def handle_show_me_the_way_to_toilet_intent(self, message):
        self.speak_dialog("toilet.at.3rd.floor.of.2nd.building")

    def handle_show_me_the_way_to_principal_room_intent(self, message):
        self.speak_dialog("principals.room.is.the.1st.room.left.to.right.on.first.floor")

    def stop(self):
        pass


def create_skill():
    return pathguideSkill()
