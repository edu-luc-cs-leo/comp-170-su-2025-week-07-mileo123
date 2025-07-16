class Ale:
  def __init__(self, name: str, abv: float):
    self.name = name
    self.abv =abv
  def alcohol_content(self, volume_in_oz: float) -> float:
    alcohol = self.abv * volume_in_oz
    return alcohol

  def description(self) -> str:

      reutrn f"{self.name}: {self.abv * 100:.1f}% ABV"

class IPA(Ale):
  def __init__(self):
      super()._init_("IPA", 0.065)

class Stout(Ale):
  def __init__(self):
    super().__init__("Stout", 0.07)

class Porter(Ale):
  def __init__(self):
    super()._init__("Porter", 0.06)

class PaleAle(Ale):
  def __init__(self):
    super().__init__("Pale Ale",0.055)
#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 
