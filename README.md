# Travel Itinerary Planner

## Overview

This project is a Python-based tool to help users plan their optimal travel itinerary. It calculates the best route for a trip based on user preferences, available travel days, and travel costs, ensuring the journey starts and ends at a mandatory starting point (e.g., Bogotá).

The planner leverages **exhaustive search with pruning and parallel processing** to evaluate possible itineraries efficiently while adhering to time and cost constraints.

---

## Features

- **User Preferences:** Rate each destination on a scale of 1-10 based on how much you'd like to visit.
- **Trip Duration:** Specify the total number of days available for the trip.
- **Mandatory Start/End Point:** The trip starts and ends at a user-defined point (e.g., Bogotá).
- **Optimization Criteria:**
  - Maximizes preference points.
  - Minimizes travel costs when points are tied.
- **Dynamic Itineraries:** Handles flexible destination sets and connections.

---

## Algorithm

1. **Input Gathering:**

   - Users provide:
     - Preference ratings for each destination.
     - Total days available for travel.
   - Mandatory points (e.g., Bogotá) are included in all itineraries.

2. **Exhaustive Search:**

   - Generates all subsets of destinations (up to a defined size).
   - Evaluates all permutations of each subset.

3. **Pruning:**

   - Skips routes that exceed available travel days or lack valid connections.

4. **Parallel Processing:**

   - Subset evaluations are distributed across multiple processes to enhance performance.

5. **Optimization:**
   - Maximizes total preference points.
   - Prefers itineraries with lower costs if points are tied.

---

## Usage

### Prerequisites

- Python 3.8 or above.
- The required destinations and connections are defined in a `data` file.

### Running the Code

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd travel-itinerary-planner
   ```
