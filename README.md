# Leetcode Progress Journal
Collection of personal solutions to leetcode problems

⭐ Arrays & Hashing
<br>• Contains Duplicate (easy) 6/18/2025</br>
Add each element to a set if it's already in the set reutrn True
<br>• Valid Anagram (easy) 6/18/2025</br>
Make 2 hashmaps then check if equal
<br>• Two Sum (easy) 6/18/2025</br>
Create a hashmap to store seen values (key = num, values = index). Check if the difference of the target and current number is in the hashmapp, and if it is you return a lis    with both indexes
<br>• Group Anagrams (medium) 6/18/2025</br>
Make a hashmap to check anagrams (this will be a hashmap where the values are lists). For each word put it in alphabetical order (any anagrams become the same "word"). Then     check if it's in the hashmap (initilize and increment eac index like a list .append and = [" "]) and return a list of just the values using list(hashmap.values())
