class raceCar:
    def __init__(self, instructions):
        self.position = 0
        self.speed = 1
        self.instructions = instructions

    def a_operation(self):
        self.position += self.speed
        self.speed *= 2

    def r_operation(self):
        if self.speed >= 0 :
            self.speed = - 1
        else:
            self.speed = 1
        # nothing happens to position in r operations


    def output(self):
        operations = self.instructions
        operations.lower()
        print('\nstart position ' + str(self.position))
        print('start speed ' + str(self.speed) + '\n')
        for operation in operations:
            if operation == 'a':
                self.a_operation()
                print('after a operation')
                print('position ' + str(self.position))
                print('speed ' + str(self.speed) + '\n')
            elif operation == 'r':
                self.r_operation()
                print('after r operation')
                print('position ' + str(self.position))
                print('speed ' + str(self.speed) + '\n')

        return self.position

    def target(self,value):
        steps = 0
        target_posistion = value
        ops = ""
        reverse_direction = False

        while self.position != target_posistion:
                print('looping posistion : ' + str(self.position))
                self.a_operation()
                steps += 1
                ops += "a"
                last_op_r = True
                print(ops)

                if (self.position > target_posistion) and \
                    (self.speed > 0):
                    print('looping posistion : ' + str(self.position))
                    self.r_operation()
                    steps += 1
                    last_op_r = False
                    ops+="r"
                    print(ops)
        
        print('\ntarget posistion : ' + str(target_posistion))
        print('ending posistion ' + str(self.position))
        print('operation instructions : ' + ops)
        print('number of steps taken : ' + str(steps) + '\n')

'''last leet'''
class Solution:
    def __init__(self):
        self.position = 0
        self.speed = 1

    def a_operation(self):
        self.position += self.speed
        self.speed *= 2
        print('end of a operation - speed, posistion' + str(self.speed) + ',' + str(self.position))

    def r_operation(self):
        if self.speed >= 0 :
            self.speed = - 1
        else:
            self.speed = 1
        print('end of r operation - speed, posistion' + str(self.speed) + ',' + str(self.position))
        # nothing happens to position in r operations

    def racecar(self, target: int) -> int:
        steps = 0
        target_posistion = target
        ops = ""
        reverse_direction = False

        while self.position != target_posistion:
                self.a_operation()
                steps += 1
                ops += "a"

                #if ((self.position > target_posistion)) and \
                #    (self.speed > 0):
                #    self.r_operation()
                #    last_op_r = False
                #    ops+="r"

                if  ((self.position > target_posistion)) and \
                    (self.speed > 0):
                    self.r_operation()
                    last_op_r = False
                    ops+="r"
        
        print('\ntarget posistion : ' + str(target_posistion))
        print('ending posistion ' + str(self.position))
        print('operation instructions : ' + ops)
        print('number of steps taken : ' + str(steps) + '\n')

        return len(ops)

if __name__ == "__main__":
    sammys_car = raceCar('aaara')
    #pos = sammys_car.output()
    sammys_car.target(3)
    #print(pos)