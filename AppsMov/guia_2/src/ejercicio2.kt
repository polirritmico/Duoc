fun main() {
    val foo: Int = 123
    var bar: Double = 1.0

    bar = foo + bar - foo * bar / foo
    println("foo más bar menos foo por bar dividido foo: $bar")

    println("\n-------------------------------------\n")

    var fuz: String? = "abc"
    println(fuz?)
}