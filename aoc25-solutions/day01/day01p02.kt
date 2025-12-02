fun main() {
    var currentPos = 50
    var zeroes = 0

    val result = generateSequence(::readLine).count { line ->
        val direction = line[0].toString()
        val steps = line.substring(1).toInt()

        if (direction == "L") {
            val rotation = currentPos - steps
            var fullRotationCount = (steps - currentPos + 99) / 100
            if (currentPos == 0) fullRotationCount--
            zeroes += fullRotationCount
            currentPos = ((rotation % 100) + 100) % 100
        } else {
            val rotation = currentPos + steps
            var fullRotationCount = rotation / 100
            zeroes += fullRotationCount
            currentPos = rotation % 100
            if (currentPos == 0) zeroes--
        }

        currentPos == 0
    }

    println(result + zeroes)
}