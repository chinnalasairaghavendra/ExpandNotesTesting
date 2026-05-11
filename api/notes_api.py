from api.api_client import APIClient


class NotesAPI(APIClient):
    def get_notes(self):
        return self.get("/notes")
    
    def create_note(self, title, description, category="Home"):
        payload = {
            "title": title,
            "description": description,
            "category": category
        }
        return self.post("/notes", payload)

    def delete_note(self, note_id):
        return self.delete(f"/notes/{note_id}")