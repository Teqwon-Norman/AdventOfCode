fun main() {
    var currentPos = 50
    val result = generateSequence(::readLine).count { line ->
        val direction = line[0].toString()
        val steps = line.substring(1).toInt()

        if (direction == "L") {
            val rotation = currentPos - steps
            currentPos = ((rotation % 100) + 100) % 100
        } else {
            val rotation = currentPos + steps
            currentPos = rotation % 100
        }
        currentPos == 0
    }

    println(result)
}