# virtual-user-ai

## Projektüberblick
`virtual-user-ai` ist aus der praktischen Beobachtung entstanden, dass produktive KI-Anwendungen häufig mehrfach dieselbe Kernlogik pro Zielplattform neu implementieren. Das Projekt bündelt diese Erkenntnisse in einem gemeinsamen technischen Ansatz: ein wiederverwendbarer KI-Kern mit klar getrennten Integrationsschichten für unterschiedliche Ausführungsumgebungen.

Der aktuelle Repository-Inhalt wurde aus bestehenden Arbeitsständen zusammengeführt. Der Import ist jedoch noch nicht vollständig abgeschlossen; einzelne Artefakte, Historienanteile und Querverweise werden weiterhin konsolidiert.

## Herkunft und Entstehungskontext
Die Initiative stammt aus einem iterativen Aufbauprozess mit Fokus auf:
- Vereinheitlichung von Prompting-, Orchestrierungs- und Laufzeitlogik,
- Reduktion von Plattform-spezifischer Duplikation,
- schnellerer Bereitstellung neuer Integrationen über Adapter statt Core-Forks.

Damit folgt das Projekt einem expliziten Architekturprinzip:

> **Ein gemeinsamer AI-Core, mehrere Plattform-Adapter.**

## Aktueller Projektstatus
Der Stand ist **POC-nah mit belastbarer technischer Basis**, aber noch nicht als vollständig produktionsreifes Gesamtsystem zu bewerten. Der Fokus liegt aktuell auf Stabilisierung, Vereinheitlichung und dokumentierter Nachvollziehbarkeit der Kernpfade.

### Status-Highlights
- **POC-Status:** Ein funktionsfähiger Proof of Concept liegt vor und dient als Referenz für die Zielarchitektur.
- **Dokumentationsstatus:** Dokumentation ist vorhanden, wird aber schrittweise harmonisiert und erweitert.
- **Webex-Track:** Der Integrationspfad für Webex wird aktiv geführt.
- **Media Worker:** Ein dedizierter Media-Worker-Pfad ist Bestandteil des aktuellen technischen Zuschnitts.
- **Linux-Host-Setup:** Der Betrieb auf Linux-Hosts ist als primäres Setup berücksichtigt.
- **Smoke Tests:** Basis-Smoke-Tests sind vorhanden, um zentrale End-to-End-Pfade schnell zu prüfen.
- **CI-Baseline:** Eine grundlegende CI-Basis ist eingerichtet und dient als Startpunkt für weitere Qualitäts-Gates.

## Scope v1
Die Version v1 ist als klar begrenzter, stabilisierbarer Lieferumfang definiert.

### In Scope (v1)
- Bereitstellung eines gemeinsamen AI-Core als zentrale fachliche und technische Laufzeitschicht.
- Anbindung relevanter Plattformen über klar definierte Adapter-Grenzen.
- Reproduzierbares Linux-Host-Setup für Entwicklung und Ausführung.
- Vorhandene Smoke-Test-Pfade zur schnellen Validierung zentraler Abläufe.
- CI-Baseline für automatisierte Grundprüfungen.
- Konsolidierte, belastbare Basisdokumentation für Architektur und Betrieb.

### Out of Scope (v1)
- Vollständige Plattformabdeckung aller potenziellen Zielsysteme.
- Umfassende Hardening- und Skalierungsmaßnahmen über die Baseline hinaus.
- Finalisierte End-to-End-Observability in voller Tiefe für alle Adapter.
- Vollständig abgeschlossener Repository-Import inklusive historischer Vollständigkeit.
- Breite Feature-Expansion außerhalb der für v1 definierten Kernpfade.

## Nächste Konsolidierungsschritte
- Abschluss der offenen Repository-Import-Arbeiten.
- Schließung von Dokumentationslücken entlang der Build-, Run- und Betriebsprozesse.
- Ausbau der CI-Baseline um zusätzliche Qualitäts- und Integrationsprüfungen.
- Schrittweise Härtung der Adaptergrenzen auf Basis der POC-Erkenntnisse.

## Zusammenfassung
`virtual-user-ai` befindet sich in einer kontrollierten Übergangsphase vom POC zu einem stabilen v1-Kern. Die technische Leitplanke ist gesetzt: **ein gemeinsamer AI-Core mit mehreren Plattform-Adaptern**, ergänzt durch Webex-Track, Media-Worker-Pfad, Linux-Host-Fokus, Smoke-Tests und CI-Baseline. Parallel dazu wird der noch nicht vollständig abgeschlossene Repository-Import weiter bereinigt.
