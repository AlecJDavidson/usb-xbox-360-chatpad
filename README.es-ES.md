

# Intérprete de Chatpad Xbox 360 para Raspberry Pi Pico

Este proyecto te permite interpretar comandos seriales de un chatpad Xbox 360 modificado utilizando una Raspberry Pi Pico. Para comenzar, sigue las instrucciones a continuación:

## Prerrequisitos
- Una placa Raspberry Pi Pico
- Un chatpad Xbox 360 modificado con un conector hembra de 6 pines Dupont soldado (se proporcionan instrucciones)
- ¡EL PICKIT3 DEBE SER UN PICKit3!
- CircuitPython CLI instalado

## Pasos
1. **Graba el chatpad**: Conecta el chatpad al Pickit3 y úsalo para grabar el archivo hex incluido en el chatpad. También se incluye el volcado (dump) del archivo hex original del chatpad para revertir los cambios si es necesario.
2. **Conecta el chatpad a la Pico**: Cablea el chatpad a la Raspberry Pi Pico de la siguiente manera:
   - TX del chatpad (pin 2) al pin RX de la Pico (Pin 0)
   - RX del chatpad (pin 3) al TX (pin 1) de la Pico.
   - Pin 4 del chatpad a tierra en la Pico.
   - Pin 1 del chatpad a 3.3v en la Pico.
   **Importante**: ¡No cablees el chatpad a la Pico antes de grabarlo! La Pico debe estar apagada durante este proceso, ya que una conexión serial entre ambos puede interferir con la grabación.

3. **Programa la Pico**: Utiliza el archivo .uf2 de Adafruit CircuitPython incluido en este proyecto. Luego, copia el directorio lib y el archivo code.py en la Raspberry Pi Pico, reemplazando los que ya se encuentren allí.

**Nota**: Se agregarán instrucciones detalladas y imágenes lo antes posible.

## Uso
Una vez que la Pico esté programada, debería interpretar los comandos seriales que provienen del chatpad modificado y convertirlos en pulsaciones de teclas HID.

¡Si tienes alguna pregunta o problema, no dudes en contactarnos!
