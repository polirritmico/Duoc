# Actividad

## Requerimientos

- [x] Crea una VPC y agrega dos subredes públicas en diferentes zonas de
      disponibilidad
- [ ] Configura una Internet Gateway y asígnala a la VPC
- [ ] Configura un grupo de seguridad que permita el tráfico por SSH y NFS
- [ ] En Amazon EFS crea un sistema de archivos
- [ ] Configura el acceso desde la VPC, habilitando el montaje automático
- [ ] Asigna el grupo de seguridad creado anteriormente para permitir las
      conexiones
- [ ] Lanza la instancia de EC2 de Amazon Linux en la VPC creada anteriormente
- [ ] Conéctate por SSH a la instancia y realiza el procedimiento de montaje de
      EFS
- [ ] Realiza pruebas para probar el funcionamiento de EFS
- [ ] Cree un grupo de Auto Scaling con mínimo 2 y máximo 4 instancias
- [ ] Configure de manera opcional el balanceador de carga para distribuir el
      tráfico
- [ ] Configura el Auto Scaling para el uso de CPU
- [ ] Realiza pruebas para comprobar su funcionamiento

---

## Notas

### VPC

Siempre partir creando la VPC

> [!WARNING]
>
> Siempre utilizar: **VPC and more**

### Autoscaling

Aumenta la cantidad de máquinas que sirven el servicio. Se configura el mínimo y
el máximo.

Para funcionar necesita un _template_. En AWS, vamos a:

[Launch Templates](https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#LaunchTemplates:)

Crear las instancias en el mismo grupo de subred que la instancia original.

Recordar asignar ip pública.

Al crear grupo de AutoScaling, usar la plantilla.

El valor del umbral se calcula en base al promedio de todas las instancias en
funcionamiento.

### IPv4 VPC CIDR blocks

Lista de rangos de ejemplo:

| RFC 1918 range                                    | CIDR block     |
| ------------------------------------------------- | -------------- |
| 10.0.0.0 - 10.255.255.255 (10/8 prefix)           | 10.0.0.0/16    |
| 172.16.0.0 - 172.31.255.255 (172.16/12 prefix)    | 172.31.0.0/16  |
| 192.168.0.0 - 192.168.255.255 (192.168/16 prefix) | 192.168.0.0/20 |

## Notas creación

> Tag `preparación`

- **VPC:**
  - id: vpc-0bd19ad90c37ab250
  - IPv4 CIDR: 172.31.0.0/24
- **Subnets:**
  - :
  - :
- **Getaway:**
  - id:
  - name:
- **Security Group:**
  - id:
  - name:
- EFS:
  - id:
  - name:
  - mount: `command`
- Instancia 1:
  - name:
  - ip:
