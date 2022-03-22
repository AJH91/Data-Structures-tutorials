class TreeNode:
    def __init__(self,name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child_to_add):
        child_to_add.parent = self
        self.children.append(child_to_add)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level+= 1
            p = p.parent
        return level

    def print_tree_level(self, levelRange):
          spaces = '  ' * self.get_level() * 3
          print(spaces + self.name)
          if len(self.children) <= levelRange:
                for child in self.children:
                    child.print_tree_level(levelRange)


    def print_tree(self, type):
        if type == "name":
            spaces = '  ' * self.get_level() * 3
            print(spaces + self.name)
            if (self.children):
                for child in self.children:
                    child.print_tree(type)
        elif type == "designation":
            spaces = '  ' * self.get_level() * 3
            print(spaces + self.designation)
            if (self.children):
                for child in self.children:
                    child.print_tree(type)
        elif type=="both":
            spaces = '  ' * self.get_level() * 3
            print(spaces + self.name + " " + "(" + (self.designation) + ")")
            if (self.children):
                for child in self.children:
                    child.print_tree(type)


def build_product_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Screen"))
    laptop.add_child(TreeNode("Battery Pack"))
    root.add_child(laptop)
    return root

def build_hierarchy_tree():
    root = TreeNode("Nilupul", "CEO")
    second_lvl = TreeNode("Chinmay", "CTO")
    third_level = TreeNode("Vishwa", "Infrastructure Head")
    fourth_level_a = TreeNode("Dhaval", "Cloud Manager")
    fourth_level_b = TreeNode("Abhijit", "App Manager")
    third_level_a = TreeNode("Aamir", "Application Head")
    third_level_b = TreeNode("Gels", "HR head")
    fourth_level_c = TreeNode("Peter", "Recruitment Manager")
    fourth_level_d = TreeNode("Waqas", "Policy Manager")

    root.add_child(second_lvl)
    second_lvl.add_child(third_level)
    third_level.add_child(fourth_level_a)
    third_level.add_child(fourth_level_b)
    third_level.add_child(third_level_a)
    second_lvl.add_child(third_level_b)
    third_level_b.add_child(fourth_level_c)
    third_level_b.add_child(fourth_level_d)
    return root

if __name__ == '__main__':
     #root = build_product_tree()
     #root.print_tree()

     root = build_hierarchy_tree()
     #root.print_tree("name")
     #root.print_tree("designation")
     #root.print_tree("both")
     root.print_tree_level(3)



