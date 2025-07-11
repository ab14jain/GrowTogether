package out.production.OPPsConcept.Class98;

public class ArrayIndexOutOfBounds {
    
    public static int accessArrayElement(int[] array, int index) {
        //code here
        try{
            return array[index];
        }
        catch(ArrayIndexOutOfBoundsException ex){
            return -1;
        }
    }
    
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5};

        int index = 6;
        int result = accessArrayElement(array, index);
        if(result!=-1){
            System.out.println("The value stored at index "+index+" is "+result);
        }

        index = 4;
        result = accessArrayElement(array, index);
        if(result!=-1){
            System.out.println("The value stored at index "+index+" is "+result);
        }

        index = 5;
        result = accessArrayElement(array, index);
        if(result!=-1){
            System.out.println("The value stored at index "+index+" is "+result);
        }

        index = 0;
        result = accessArrayElement(array, index);
        if(result!=-1){
            System.out.println("The value stored at index "+index+" is "+result);
        }

        index = -2;
        result = accessArrayElement(array, index);
        if(result!=-1){
            System.out.println("The value stored at index "+index+" is "+result);
        }

        index = 3;
        result = accessArrayElement(array, index);
        if(result!=-1){
            System.out.println("The value stored at index "+index+" is "+result);
        }

        index = -1;
        result = accessArrayElement(array, index);
        if(result!=-1){
            System.out.println("The value stored at index "+index+" is "+result);
        }

        index = 10;
        result = accessArrayElement(array, index);
        if(result!=-1){
            System.out.println("The value stored at index "+index+" is "+result);
        }

        int arr[] = {0,5,3,8,9,10000,98432,98127,1243834,233};

        index = 0;
        result = accessArrayElement(arr, index);
        if(result!=-1){
            System.out.println("The value stored at index "+index+" is "+result);
        }

        index = 3;
        result = accessArrayElement(arr, index);
        if(result!=-1){
            System.out.println("The value stored at index "+index+" is "+result);
        }

        index = 9;
        result = accessArrayElement(arr, index);
        if(result!=-1){
            System.out.println("The value stored at index "+index+" is "+result);
        }

        index = 6;
        result = accessArrayElement(arr, index);
        if(result!=-1){
            System.out.println("The value stored at index "+index+" is "+result);
        }
    }
}
