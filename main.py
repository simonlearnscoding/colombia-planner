import threading  # For managing background tasks
import tkinter as tk
from tkinter import ttk  # For progress bar
from tkinter import messagebox

from PIL import Image, ImageTk  # For rendering images

from data import bogota, destinations  # Import your destinations
from logic import calculate_itinerary, format_itinerary


class HolidayPlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Holiday Planner")
        self.root.configure(bg="#2e2e2e")  # Dark background

        self.days_available = 0
        self.current_destination_index = 0
        self.destination_preferences = {}
        self.current_rating = None

        # Initialize GUI
        self.setup_gui()

    def setup_gui(self):
        font_large = ("Arial", 16)
        font_medium = ("Arial", 14)

        # Create main frame for vertical alignment
        self.main_frame = tk.Frame(self.root, bg="#2e2e2e")
        self.main_frame.pack(expand=True)

        # Trip duration input
        self.duration_label = tk.Label(
            self.main_frame, text="Enter Trip Duration (days):", font=font_large, bg="#2e2e2e", fg="white"
        )
        self.duration_label.pack(pady=10)

        self.duration_entry = tk.Entry(self.main_frame, font=font_medium)
        self.duration_entry.pack(pady=10)
        self.duration_entry.bind("<Return>", self.start_rating)  # Bind Enter key to start rating

        self.start_button = tk.Button(
            self.main_frame, text="Start Rating Destinations", font=font_medium, bg="#555", fg="white",
            command=self.start_rating
        )
        self.start_button.pack(pady=20)

        # Destination rating widgets (hidden initially)
        self.destination_frame = tk.Frame(self.main_frame, bg="#2e2e2e")
        self.destination_image_label = tk.Label(self.destination_frame, bg="#2e2e2e")
        self.destination_image_label.pack()

        self.destination_title_label = tk.Label(
            self.destination_frame, font=font_large, bg="#2e2e2e", fg="white"
        )
        self.destination_title_label.pack(pady=10)

        self.destination_description_label = tk.Label(
            self.destination_frame, wraplength=400, font=font_medium, bg="#2e2e2e", fg="white"
        )
        self.destination_description_label.pack(pady=10)

        self.rating_label = tk.Label(
            self.destination_frame, text="Rate this destination (1-10):", font=font_large, bg="#2e2e2e", fg="white"
        )
        self.rating_label.pack(pady=10)

        self.rating_entry = tk.Entry(self.destination_frame, font=font_medium)
        self.rating_entry.pack(pady=10)
        self.rating_entry.bind("<Return>", self.submit_rating)  # Bind Enter key to submit rating

        self.destination_frame.pack_forget()

        # Loading screen
        self.loading_frame = tk.Frame(self.main_frame, bg="#2e2e2e")
        self.loading_label = tk.Label(
            self.loading_frame, text="Calculating itinerary, please wait...", font=font_large, bg="#2e2e2e", fg="white"
        )
        self.loading_label.pack(pady=20)
        self.progress_bar = ttk.Progressbar(self.loading_frame, mode="indeterminate")
        self.progress_bar.pack(pady=10, fill=tk.X)
        self.loading_frame.pack_forget()

        # Results display (hidden initially)
        self.results_box = tk.Text(
            self.main_frame,
            wrap=tk.WORD,
            width=60,
            height=20,
            font=font_medium,
            bg="#2e2e2e",
            fg="white",
            padx=15,  # Add padding inside the text box (horizontal)
            pady=15   # Add padding inside the text box (vertical)
        )
        self.results_box.pack(pady=20, padx=20)  # Add padding between the text box and its surroundings
        self.results_box.pack_forget()
        self.results_box.pack_forget()

    def start_rating(self, event=None):
        try:
            self.days_available = int(self.duration_entry.get())
            if self.days_available <= 0:
                raise ValueError("Days must be greater than 0.")
            self.duration_label.pack_forget()
            self.duration_entry.pack_forget()
            self.start_button.pack_forget()
            self.show_next_destination()
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def show_next_destination(self):
        if self.current_destination_index < len(destinations):
            destination = destinations[self.current_destination_index]
            self.display_destination(destination)
        else:
            self.show_loading_screen()

    def display_destination(self, destination):
        self.destination_frame.pack()
        self.rating_entry.delete(0, tk.END)  # Clear the rating entry field
        self.destination_title_label.config(text=destination.title)
        self.destination_description_label.config(text=destination.description)

        # Load and display the image
        try:
            normalized_title = destination.title.lower().replace(" ", "_").replace("é", "e").replace("í", "i").replace("á", "a")
            image_path = f"./images/{normalized_title}.jpg"
            print("image path:", image_path)
            image = Image.open(image_path)
            image = image.resize((400, 300), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            self.destination_image_label.config(image=photo)
            self.destination_image_label.image = photo
        except FileNotFoundError:
            self.destination_image_label.config(text="[Image not available]")
            self.destination_image_label.image = None

    def submit_rating(self, event=None):
        try:
            rating = int(self.rating_entry.get())
            if not (1 <= rating <= 10):
                raise ValueError("Please enter a number between 1 and 10.")
            self.rate_destination(rating)
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def rate_destination(self, rating):
        destination = destinations[self.current_destination_index]
        self.destination_preferences[destination.title] = rating
        destination.preference_points = rating
        self.current_destination_index += 1
        self.show_next_destination()

    def show_loading_screen(self):
        self.destination_frame.pack_forget()
        self.loading_frame.pack()
        self.progress_bar.start(10)  # Start the progress bar animation
        threading.Thread(target=self.calculate_itinerary).start()  # Run calculation in background

    def calculate_itinerary(self):
        # Calculate the best itinerary
        mandatory_points = [bogota]  # Ensure the trip starts and ends in Bogotá
        best_itinerary, points, cost, total_travel_time = calculate_itinerary(
            destinations, bogota, self.days_available, mandatory_points
        )

        self.loading_frame.pack_forget()  # Hide loading screen
        self.progress_bar.stop()

        # Display results
        self.results_box.pack()
        if best_itinerary:
            itinerary_text = format_itinerary(best_itinerary, mandatory_points)
            self.results_box.insert(tk.END, itinerary_text)
            self.results_box.insert(tk.END, f"\nTotal Preference Points: {points}")
            self.results_box.insert(tk.END, f"\nTotal Travel Cost: ${cost}")
            self.results_box.insert(tk.END, f"\nTotal Travel Time: {total_travel_time} days")
        else:
            self.results_box.insert(tk.END, "No feasible itinerary found.")


# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = HolidayPlanner(root)
    root.mainloop()
