fun main() {
    val input = generateSequence(::readLine).toList()
    val emptyLineIdx = input.indexOf("")

    val ranges = input.subList(0, emptyLineIdx).map { line ->
        val (a, b) = line.split("-")
        Pair(a.toLong(), b.toLong())
    }.sortedBy { it.first }

    println(
        ranges.fold(mutableListOf<Pair<Long, Long>>()) { acc, range ->
            if (acc.isEmpty() || acc.last().second < range.first) {
                acc.add(range)
            } else {
                val last = acc.removeAt(acc.size - 1)
                acc.add(Pair(last.first, maxOf(last.second, range.second)))
            }
            acc
        }.sumOf { (it.second - it.first) + 1}
    )
}