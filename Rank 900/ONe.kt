import kotlin.math.pow

fun findP(x: Int, y: Int): Int {
    var i = 0
    while (i < 10) {
        val value = x * (10.0.pow(i)).toInt()
        if (value > y) {
            return y - (x * (10.0.pow(i - 1)).toInt())
        } else if (value == y) {
            return 0
        }
        i++
    }
    return 0
}

fun main() {
    val t = readLine()!!.toInt()
    repeat(t) {
        val (x, y) = readLine()!!.split(" ").map { it.toInt() }
        var step = 0
        var yValue = y
        while (yValue != 0) {
            if (yValue < x) {
                step += yValue
                break
            }
            if (yValue == 1) {
                yValue = 0
                step += 1
                break
            }
            val nextYValue = findP(x, yValue)
            if (nextYValue == 0) {
                step += 1
                break
            }
            step += yValue / x
            yValue %= x
        }
        println(step)
    }
}
