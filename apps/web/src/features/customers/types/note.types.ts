export type Note = {
  id: string;
  customer_id: string;
  author_id: string | null;
  content: string;
  created_at: string;
  updated_at: string;
};

export type NoteCreate = {
  content: string;
};

export type NoteUpdate = {
  content?: string;
};