import kotlin.math.abs

fun main() {
    val result = generateSequence(::readLine).count { line ->
        val nums = line.split("\\s+".toRegex()).map { it.toInt() }
        val asc = nums.windowed(2).all { (first, second) ->
            first < second && abs(first - second) in 1..3 
        }

        val desc = nums.windowed(2).all { (first, second) ->
            first > second && abs(first - second) in 1..3 
        }
        
        asc || desc
    }
    println(result)
}