sealed class ResultadoLogin {
    data class Exito(val perfil: PerfilUsuario) : ResultadoLogin()
    data class Error(val msg: String) : ResultadoLogin()
    object autenticando: ResultadoLogin ()
}