fun main() {
    val input = generateSequence(::readLine).toList()
    val emptyLineIdx = input.indexOf("")

    val ranges = input.subList(0, emptyLineIdx).map { line ->
        val (a, b) = line.split("-")
        Pair(a.toLong(), b.toLong())
    }.sortedBy { it.first }

    val nums = input.subList(emptyLineIdx + 1, input.size)
        .map { it.toLong() }
        .sorted()

    var rangeIdx = 0
    println(
        nums.count { num ->
            while (rangeIdx < ranges.size && ranges[rangeIdx].second < num) {
                rangeIdx++
            }
            rangeIdx < ranges.size && num >= ranges[rangeIdx].first && num <= ranges[rangeIdx].second
        }
    )
}