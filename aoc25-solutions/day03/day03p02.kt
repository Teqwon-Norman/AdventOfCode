fun getMaxNum(nums: String): Long {
    val indices = mutableListOf<Int>()
    val n = 12

    for (i in 0 until n) {
        val start = if (indices.isEmpty()) 0 else indices.last() + 1
        val end = nums.length - (n - i)

        var maxPair = Pair(0, start)
        for (idx in start..end) {
            val digit = nums[idx].digitToInt()
            if (digit > maxPair.first) {
                maxPair = Pair(digit, idx)
            }
        }
        indices.add(maxPair.second)
    }
    return indices.map { nums[it] }.joinToString("").toLong()
}

fun main() {
    println(
        generateSequence(::readLine).sumOf(::getMaxNum)
    )
}