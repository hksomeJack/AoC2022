# Advent of Code: Day 1, Counting Calories

# Advent of Code: Day 1

## Elf Carrying the Most Calories
[Original Problem on AoC](https://adventofcode.com/2022/day/1)

I feel attacked from the get. Counting calories, this close to Christmas? How dare you. This is the month where self-monitoring ceases and everyone let's everybody else stop thinking about their weight. As an ardent Decemberist who thinks all should be jolly/merry and fat this month, I almost adbstained in principle. Alas, almost. Here we go.

Since I hadn't programmed in a while (work, life, etc [that covers all categories anyways]), I just went with a couple for loops. I played with the idea of using map() and lambdas, but ultimately felt too stupid to make that work. COVID-19 hit hard a week ago and the black cloud is still hanging around -- and I ain't that bright to begin with.


'''bash
   for i in range(len(total_calories_list)):
        #print(total_calories_list[i])
        if total_calories_list[i] > max_value:
            max_value = total_calories_list[i]
        else:
            continue
'''

## Total for the Top Three Elves

I also initially forgot about the sorted() function, was iterating through list and comparing values to start. Derp. Employed sorted() and then did the obvious -- sliced and summed the top 3. 