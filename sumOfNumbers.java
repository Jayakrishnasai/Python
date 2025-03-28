import java.util.Scanner;
public class sumOfNumbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the first number: ");
        int m = sc.nextInt();
        System.out.print("Enter the second number: ");
        int n = sc.nextInt(); 
        int sum = 0;
        for (int i = m; i <= n; i++) {
            sum += i;
        }
        System.out.println("Sum of Numbers from " + m + " to " + n + " is: " + sum);
        sc.close();
    }
}
