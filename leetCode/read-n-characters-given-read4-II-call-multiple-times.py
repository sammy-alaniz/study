'''
Link: https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/

Given a file and assume that you can only read the file using a given method read4, implement a method read to read n characters. Your method read may be called multiple times.

Method read4:

The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf4
    Returns:    int

buf4[] is a destination, not a source. The results from read4 will be copied to buf4[].
Below is a high-level example of how read4 works:


File file("abcde"); // File is "abcde", initially file pointer (fp) points to 'a'
char[] buf4 = new char[4]; // Create buffer with enough space to store characters
read4(buf4); // read4 returns 4. Now buf4 = "abcd", fp points to 'e'
read4(buf4); // read4 returns 1. Now buf4 = "e", fp points to end of file
read4(buf4); // read4 returns 0. Now buf4 = "", fp points to end of file
 

Method read:

By using the read4 method, implement the method read that reads n characters from file and store it in the buffer array buf. Consider that you cannot manipulate file directly.

The return value is the number of actual characters read.

Definition of read:

    Parameters:	char[] buf, int n
    Returns:	int

buf[] is a destination, not a source. You will need to write the results to buf[].
Note:

Consider that you cannot manipulate the file directly. The file is only accessible for read4 but not for read.
The read function may be called multiple times.
Please remember to RESET your class variables declared in Solution, as static/class variables are persisted across multiple test cases. Please see here for more details.
You may assume the destination buffer array, buf, is guaranteed to have enough space for storing n characters.
It is guaranteed that in a given test case the same buffer buf is called by read.
 

Example 1:

Input: file = "abc", queries = [1,2,1]
Output: [1,2,0]
Explanation: The test case represents the following scenario:
File file("abc");
Solution sol;
sol.read(buf, 1); // After calling your read method, buf should contain "a". We read a total of 1 character from the file, so return 1.
sol.read(buf, 2); // Now buf should contain "bc". We read a total of 2 characters from the file, so return 2.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
Assume buf is allocated and guaranteed to have enough space for storing all characters from the file.
Example 2:

Input: file = "abc", queries = [4,1]
Output: [3,0]
Explanation: The test case represents the following scenario:
File file("abc");
Solution sol;
sol.read(buf, 4); // After calling your read method, buf should contain "abc". We read a total of 3 characters from the file, so return 3.
sol.read(buf, 1); // We have reached the end of file, no more characters can be read. So return 0.
 

Constraints:

1 <= file.length <= 500
file consist of English letters and digits.
1 <= queries.length <= 10
1 <= queries[i] <= 500



'''

# My attempt at solution, works if n is less than 4 needs work
# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

# 1 - call read4, and place recieved chars into class array
# 2 - based on what was requested, return the chars and num read
#   - if there is nothing to return, then return nothing
# 3 - book keep what has been returned, and if nothing keep it at nothing
class Sammys_Solution_Didnt_work:

    def __init__(self) -> None:
        print('\ninit hit')
        self.what_Ive_read = []
        self.what_Ive_returned = 0

    def addCharsToBuf(self, new_buf: List[str], original_buf: List[str]):
        for i in range(len(original_buf)):
            original_buf[i] = ''

        for i in range(len(new_buf)):
            original_buf[i] = new_buf[i]

    def read(self, buf: List[str], n: int) -> int:
        print('\nread hit')

        num = read4(buf)
        if num != 0 :
            for i in range(num):
                self.what_Ive_read.append(buf[i])
            
            new_buf = []
            
            for i in range(self.what_Ive_returned, self.what_Ive_returned + n):
                if i <= len(self.what_Ive_read) - 1:
                    new_buf.append(self.what_Ive_read[i])
            
            self.what_Ive_returned += n

            print('what_Ive_returned : ', self.what_Ive_returned)
            print('new_buf', new_buf)

            self.addCharsToBuf(new_buf, buf)

            return len(new_buf)

        else:
            new_buf = []

            for i in range(self.what_Ive_returned, self.what_Ive_returned + n):
                if i <= len(self.what_Ive_read) - 1:
                    new_buf.append(self.what_Ive_read[i])
            
            self.what_Ive_returned += n

            print('what_Ive_returned : ', self.what_Ive_returned)
            print('new_buf', new_buf)

            self.addCharsToBuf(new_buf, buf)

            return len(new_buf)

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

# 1 - call read4, and place recieved chars into class array
# 2 - based on what was requested, return the chars and num read
#   - if there is nothing to return, then return nothing
# 3 - book keep what has been returned, and if nothing keep it at nothing



class Sammys_Solution_WORKS:

    def __init__(self) -> None:
        print('\ninit hit')
        self.what_Ive_read = []
        self.what_Ive_returned = 0

    def addCharsToBuf(self, new_buf: List[str], original_buf: List[str]):
        for i in range(len(original_buf)):
            original_buf[i] = ''

        for i in range(len(new_buf)):
            original_buf[i] = new_buf[i]

    def iterations(self, n: int) -> int:
        print('\niterations hit', int(n/4) + (n % 4 > 0 ))
        return int(n/4) + (n % 4 > 0 )

    def read(self, buf: List[str], n: int) -> int:
        print('\nread hit')
        print('number of chars : ', n)

        new_buf = []

        for _ in range(self.iterations(n)):
            print('iteration : ', _)
            num = read4(buf)
            print('num : ', num)

            if num != 0 :
                for i in range(num):
                    self.what_Ive_read.append(buf[i])

        print('what ive read : ', self.what_Ive_read)

        for j in range(self.what_Ive_returned, self.what_Ive_returned + n):
            if j <= len(self.what_Ive_read) - 1:
                new_buf.append(self.what_Ive_read[j])

        self.what_Ive_returned += n

        self.addCharsToBuf(new_buf, buf)

        return len(new_buf)

