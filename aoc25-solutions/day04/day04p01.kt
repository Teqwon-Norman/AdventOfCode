fun getAllCoordsSet(input: List<String>): Set<Pair<Int, Int>> =
    input.withIndex()
        .flatMap { (row, line) ->
            line.withIndex()
                .mapNotNull { (col, char) ->
                    if (char == '@') Pair(row, col) else null
                }
        }
        .toSet()

val directions = listOf(
    -1 to -1, -1 to 0, -1 to 1,
    0 to -1, 0 to 1,
    1 to -1, 1 to 0, 1 to 1
)

fun countNeighbors(coord: Pair<Int, Int>, allCoords: Set<Pair<Int, Int>>): Int {
    val (row, col) = coord
    return directions.count { (dr, dc) ->
        Pair(row + dr, col + dc) in allCoords
    }
}

fun main() {
    val lines = generateSequence(::readLine).toList()
    val allCoords = getAllCoordsSet(lines)

    println(
        allCoords.count { coord ->
            countNeighbors(coord, allCoords) < 4
        }
    )
}