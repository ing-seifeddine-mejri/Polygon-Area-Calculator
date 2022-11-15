class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height
  
  def __str__(self):
    str_width = str(self.width)
    str_height = str(self.height)
    return 'Rectangle(width=' + str_width + ', height=' + str_height + ')'

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height 

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** 0.5

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return 'Too big for picture.'
    else:
      return ("*" * self.width + "\n") * self.height
  
        
  def get_amount_inside(self, shape):
    ins_width = self.width // shape.width
    ins_height = self.height // shape.height
    return ins_width * ins_height


class Square(Rectangle):

  def __init__(self, side):
    super().__init__(side,side)

  def __str__(self):
    str_width = str(self.width)
    str_height = str(self.height)
    if str_width == str_height:
      return 'Square(side=' + str_width + ')'

  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self, width):
    self.set_side(width)

  def set_height(self, height):
    self.set_side(height)