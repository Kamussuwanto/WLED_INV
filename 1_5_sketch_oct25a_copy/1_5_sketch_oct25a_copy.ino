#include <WiFi.h>
#include <WebServer.h>
#include <ESPmDNS.h>
#include <Adafruit_NeoPixel.h>

// Hardware Configurations
#define LED_PIN     18   // Pin connected to the WS2812B Data line
#define NUM_LEDS    50   // Total number of drawers/LEDs
Adafruit_NeoPixel strip(NUM_LEDS, LED_PIN, NEO_GRB + NEO_KHZ800);

// Wi-Fi Parameters
const char* ssid = "AndroidAPB82E";
const char* password = "aaaaDddd";

WebServer server(80);

void handleLight() {
  if (server.hasArg("led")) {
    int target_led = server.arg("led").toInt();
    if (target_led >= 0 && target_led < NUM_LEDS) {
      strip.clear();
      // Green flash (R=0, G=255, B=0)
      strip.setPixelColor(target_led, strip.Color(0, 255, 0)); 
      strip.show();
      server.send(200, "text/plain", "OK: Lit up LED " + String(target_led));
      return;
    }
  }
  server.send(400, "text/plain", "Missing or invalid 'led' parameter");
}

void setup() {
  Serial.begin(115200);
  delay(500); // Give the serial connection time to stabilize
  Serial.println("\nInitializing System...");

  // Initialize LED Strip safely at low brightness
  strip.begin();
  strip.setBrightness(30); // KEEP LOW (30 out of 255) to reduce boot current draw
  strip.clear();
  strip.show();

  // Connect to Local Wi-Fi Network
  WiFi.begin(ssid, password);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("");
  Serial.print("Connected! IP address: ");
  Serial.println(WiFi.localIP());

  // Initialize mDNS Service
  if (!MDNS.begin("electronics-leds")) { 
    Serial.println("Error setting up MDNS responder!");
  } else {
    Serial.println("mDNS responder started: electronics-leds.local");
    MDNS.addService("http", "tcp", 80);
  }

  // Setup Web Server Endpoints
  server.on("/light", HTTP_GET, handleLight);
  server.begin();
  Serial.println("HTTP Server started");
}

void loop() {
  server.handleClient();
  delay(1); // Yield execution briefly to core background tasks
}
