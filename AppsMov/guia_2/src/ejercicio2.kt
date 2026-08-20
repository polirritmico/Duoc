fun main() {
    val numeros = listOf(1, 2, 3, 4, 5)
    val pares = numeros.filter {
        it % 2 == 0 && it > 2
    }
    println(pares) // [2, 4]
}