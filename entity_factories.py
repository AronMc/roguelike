from components.ai import HostileEnemy
from components import consumable
from components.fighter import Fighter
from components.inventory import Inventory
from entity import Actor, Item

player = Actor(
    char ="@",
    color=(255, 255, 255),
    name="LabMouse",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=3, defense=2, power=5),
    inventory=Inventory(capacity=2),
)

mouse = Actor(
    char="m",
    color=(63, 127, 63),
    name="Mouse",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=1, defense=0, power=3),
    inventory=Inventory(capacity=0),
)
rat = Actor(
    char="R",
    color=(0, 127, 0),
    name="Rat",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=2, defense=1, power=4),
    inventory=Inventory(capacity=0)
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
    consumable=consumable.BatteryDamageConsumable(damage=1, maximum_range=2),
)