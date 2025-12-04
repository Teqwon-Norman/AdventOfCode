fun getMaxPair(nums: String): Int {
    var firstMax = Pair(-1, -1)
    var secondMax = Pair(-1, -1)

    for (i in 0 until nums.length - 1) {
        val digit = nums[i].digitToInt()
        if (digit > firstMax.first) {
            firstMax = Pair(digit, i)
        }
    }

    for (i in firstMax.second + 1 until nums.length) {
        val digit = nums[i].digitToInt()
        if (digit > secondMax.first) {
            secondMax = Pair(digit, i)
        }
    }
    return firstMax.first * 10 + secondMax.first
}

fun main() {
    println(
        generateSequence(::readLine).sumOf(::getMaxPair)
    )
}