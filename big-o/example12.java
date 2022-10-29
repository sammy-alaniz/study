public class example12 {

    static void permutation(String str) 
    {
        permutation(str,"");
    }

    static void permutation(String str, String prefix)
    {
        if(str.length() == 0)
        {
            System.out.println(prefix);
        }
        else
        {
            for(int i = 0; i < str.length(); i++)
            {
                String rem = str.substring(0, i) + str.substring(i+1);
                System.out.println("recursion");
                permutation(rem, prefix + str.charAt(i));
            }
        }
    }

    public static void main(String[] args) throws Exception {
        System.out.println("test");
        permutation("abcd");
    }
}