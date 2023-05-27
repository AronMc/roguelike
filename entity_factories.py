from components.ai import HostileEnemy
from components import consumable
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item

player = Actor(
    char ="@",
    color=(255, 255, 255),
    name="LabMouse",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=3, defense=2, power=5),
    inventory=Inventory(capacity=4),
    level=Level(level_up_base=4,)
)

mouse = Actor(
    char="m",
    color=(63, 127, 63),
    name="Mouse",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=1, defense=0, power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=1),
)
rat = Actor(
    char="R",
    color=(0, 127, 0),
    name="Rat",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=2, defense=1, power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=2),
    )

confusion_gas = Item(
    char="~",
    color=(207, 63, 255),
    name="Confusion Gas",
    consumable=consumable.ConfusionConsumable(number_of_turns=2),
)

napalm_pack = Item(
    char="~",
    color=(255, 0, 0),
    name="Napalm Pack",
    consumable=consumable.NapalmDamageConsumable(damage=6, radius=2),
)

health_stim = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Stim",
    consumable=consumable.HealingConsumable(amount=2)
)
battery_pack = Item(
    char="~",
    color=(255, 255, 0),
    name="Battery Pack",
    consumable=consumable.BatteryDamageConsumable(damage=7, maximum_range=3),
)