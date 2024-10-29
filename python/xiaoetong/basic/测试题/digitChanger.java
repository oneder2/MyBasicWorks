public class digitChanger{
    public static void main(String args[]){
        // initialize the input
        int fromBase = 10;
        int toBase = 2;
        int fromNum = 18;

        int length = (char)fromNum;
        int [] numList= new int[length];
        
        // reverse numList

        // input to Base10
        int base10 = 0;
        for (int digit; digit < length; digit++)
            base10 += (numList[digit]) * fromBase ^ digit;

        // // initialize the result
        // char result;

        // // Base10 to output
        // int mid = base10;
        // char mod;
        // while (mid > 0){
        //     mod = (char)(mid % toBase); // mod 取模
        //     result = mod + result; // 进位
        //     mid = mid // toBase
        // }

        System.out.println(base10);
    }
}