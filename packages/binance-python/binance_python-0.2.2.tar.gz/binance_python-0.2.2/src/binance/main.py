from dataclasses import dataclass
from binance import Spot, UserStream, User, SimpleEarn, Margin, Wallet
from binance.util import UserMixin

@dataclass
class Binance(UserMixin):
  def __post_init__(self):
    self.spot = Spot(self.api_key, self.api_secret)
    self.margin = Margin(self.api_key, self.api_secret)
    self.user_stream = UserStream(self.api_key, self.api_secret)
    self.user = User(self.api_key, self.api_secret)
    self.simple_earn = SimpleEarn(self.api_key, self.api_secret)
    self.wallet = Wallet(self.api_key, self.api_secret)
    