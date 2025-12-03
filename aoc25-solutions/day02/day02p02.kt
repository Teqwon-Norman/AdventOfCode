fun hasOccurrence(num: String): Boolean {
    val numLength = num.length

    for (i in 1..numLength / 2) {
        val pattern = num.substring(0, i)
        if (numLength % pattern.length == 0) {
            val expectedRepetitions = numLength / pattern.length
            if (pattern.repeat(expectedRepetitions) == num) {
                return true
            }
        }
    }
    return false
}

fun main() {
    val result = readLine()
        ?.split(",")
        ?.flatMap { numRange ->
            val (first, second) = numRange.split("-").map { it.toLong() }
            (first..second).toList() }
        ?.filter {
            val numString = it.toString()
            hasOccurrence(numString)
        }?.sum()
    println(result)
}