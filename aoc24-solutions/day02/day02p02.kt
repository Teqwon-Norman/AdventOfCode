import kotlin.math.abs

fun is_safe(nums: List<Int>): Boolean {
    val asc = nums.windowed(2).all { (first, second) ->
        first < second && abs(first - second) in 1..3 
    }
    val desc = nums.windowed(2).all { (first, second) ->
        first > second && abs(first - second) in 1..3 
    }
    return asc || desc
}

fun main() {
    val result = generateSequence(::readLine).count { line ->
        val nums = line.split("\\s+".toRegex()).map { it.toInt() }
        nums.indices.any {
            is_safe(nums.take(it) + nums.drop(it + 1))
        }
    }
    println(result)
}