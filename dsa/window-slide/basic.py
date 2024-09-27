a = [9,20,2,3,3,4,5,5,6,6,7,40]
k = 3
i = 0
currentSum = 0
maxSum = 0
while(i<k):
    currentSum = currentSum+a[i]
    i = i+1
i = k
print(currentSum)
maxSum = currentSum

while(i<len(a)):
    currentSum = (currentSum+a[i])-a[i-k]
    i = i+1
    maxSum = max(currentSum,maxSum)

print(maxSum)


def get_max_sum(arr, k):
    current_sum = sum(arr[:k])  # Initial sum of the first 'k' elements
    max_sum = current_sum

    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]  # Slide the window
        max_sum = max(max_sum, current_sum)  # Update max_sum if current_sum is greater

    return max_sum

# Example usage
a = [20,10, 3, 3, 4, 5, 5, 6, 6, 7]
k = 2
result = get_max_sum(a, k)
print(result)

        
    