import { api } from "@/lib/api/client";

import type {
  Note,
  NoteCreate,
  NoteUpdate,
} from "../types/note.types";

export const NoteService = {
  async getCustomerNotes(
    customerId: string,
  ): Promise<Note[]> {
    const response = await api.get<Note[]>(
      `/customers/${customerId}/notes`,
    );

    return response.data;
  },

  async createNote(
    customerId: string,
    data: NoteCreate,
  ): Promise<Note> {
    const response = await api.post<Note>(
      `/customers/${customerId}/notes`,
      data,
    );

    return response.data;
  },

  async updateNote(
    customerId: string,
    noteId: string,
    data: NoteUpdate,
  ): Promise<Note> {
    const response = await api.patch<Note>(
      `/customers/${customerId}/notes/${noteId}`,
      data,
    );

    return response.data;
  },

  async deleteNote(
    customerId: string,
    noteId: string,
  ): Promise<void> {
    await api.delete(
      `/customers/${customerId}/notes/${noteId}`,
    );
  },
};