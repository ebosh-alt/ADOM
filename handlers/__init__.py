from .greeting import greeting_rt
from .payments import payments_rt
from .help import help_rt
from .subscription import subscription_rt

routers = (greeting_rt, payments_rt, help_rt, subscription_rt)
