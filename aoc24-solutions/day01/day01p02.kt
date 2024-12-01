import java.util.Scanner

fun getSimilarity(h1: MutableList<Int>, h2: Map<Int, Int>): Int {
    var total = 0
    for (i in 0 until h1.size) {
        total += (h1[i] * h2.getOrDefault(h1[i], 0))
    }
    return total
}

fun main() {
    val file = Scanner(System.`in`)
    val s1 = mutableListOf<Int>()
    val s2 = mutableListOf<Int>()

    while (file.hasNextLine()) {
        val line = file.nextLine()
        val (first, last) = line.split("\\s+".toRegex())
        s1.add(first.toInt())
        s2.add(last.toInt())
    }

    val freq = s2.associateWith { num -> s2.count { num == it } }
    println(getSimilarity(s1, freq))
}