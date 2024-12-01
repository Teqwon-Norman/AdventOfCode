import java.util.Scanner
import java.util.PriorityQueue
import kotlin.math.*

fun getDistance(h1: PriorityQueue<Int>, h2: PriorityQueue<Int>): Int {
    var total = 0
    for (i in 0 until h1.size) {
        val a = h1.poll()
        val b = h2.poll()
        total += abs(a - b)
    }
    return total
}

fun main() {
    val reader = Scanner(System.`in`)
    val h1 = PriorityQueue<Int>()
    val h2 = PriorityQueue<Int>()

    while (reader.hasNextLine()) {
        val line = reader.nextLine()
        val (first, last) = line.split("\\s+".toRegex())
        h1.add(first.toInt())
        h2.add(last.toInt())
    }
    println(getDistance(h1, h2))
}