import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking

fun main() {
    println("Inicio")
    runBlocking {
        autenticarUsuario("admin", "123")
    }
    println("Fin")
}

suspend fun autenticarUsuario(
    usuario: String,
    contraseña: String,
) : ResultadoLogin {
    delay(2000L)
    val validUser = "admin"
    val validPass = "1234"
    if (usuario == validUser && contraseña == validPass) {
        val user: PerfilUsuario = PerfilUsuario("foo", "foo@bar.cl")
        return ResultadoLogin.Exito(user);
    }
    return ResultadoLogin.Error("Credenciales incorrectas")
}