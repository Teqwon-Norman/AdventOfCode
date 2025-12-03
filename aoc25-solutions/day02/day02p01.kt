fun main() {
    val result = readLine()
        ?.split(",")
        ?.flatMap { numRange ->
            val (first, second) = numRange.split("-").map { it.toLong() }
            (first..second).toList() }
        ?.filter {
            val numString = it.toString()
            val numLength = numString.length
            numLength % 2 == 0 &&
                numString.substring(0, numString.length / 2) == numString.substring(numString.length / 2)
        }?.sum()
    println(result)
}