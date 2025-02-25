#include <stdio.h>
#include <stdlib.h> // For rand() and srand()
#include <time.h>   // For clock() and CLOCKS_PER_SEC
// Function to perform selection sort
void selectionSort(int arr[], int n) 
{
    int i, j, min_idx;
    // One by one move boundary of unsorted subarray
    for (i = 0; i < n - 1; i++) 
    {
        // Find the minimum element in the unsorted array
        min_idx = i;
        for (j = i + 1; j < n; j++) 
        {
            if (arr[j] < arr[min_idx]) 
            {
                min_idx = j;
            }
        }
        // Swap the found minimum element with the first element
        int temp = arr[min_idx];
        arr[min_idx] = arr[i];
        arr[i] = temp;
    }
}
// Function to print an array (first 10 elements only)
void printArray(int arr[], int size) 
{
    int i;
    for (i = 0; i < 10; i++) 
    { // Print only the first 10 elements
        printf("%d ", arr[i]);
    }
    printf("\n");
}
int main() 
{
    int n;
    printf("Enter the number of elements in the array (>= 5000): ");
    scanf("%d", &n);
    if (n < 5000) 
    {
        printf("Please enter a number greater than or equal to 5000.\n");
        return 1; // Exit the program
    }
    int *arr = (int *)malloc(n * sizeof(int)); // Dynamically allocate memory for the array
    // Seed the random number generator
    srand(time(0));
    // Fill the array with random numbers
    for (int i = 0; i < n; i++) 
    {
        arr[i] = rand() % 100000; // Random numbers between 0 and 99999
    }
    printf("Original array (first 10 elements): \n");
    printArray(arr, n); 
    // Measure the time taken by selection sort
    clock_t start = clock(); // Start the clock
    selectionSort(arr, n);   // Perform selection sort
    clock_t end = clock();   // End the clock

    double time_taken = ((double)(end - start)) / CLOCKS_PER_SEC; // Calculate time in seconds

    printf("Sorted array (first 10 elements): \n");
    printArray(arr, n); // Print only the first 10 elements for brevity

    printf("Time taken by Selection Sort: %f seconds\n", time_taken);

    free(arr); // Free dynamically allocated memory
    return 0;
}
