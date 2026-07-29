/**
 * ╔══════════════════════════════════════════════════════════════════╗
 * ║                                                                  ║
 * ║   ░█▀▀░▀█▀░█▀▀░█░░░█▀█   ░█▀▄░█▀▀░█░█░█▀▀                     ║
 * ║   ░▀▀█░░█░░█▀▀░█░░░█▀█   ░█░█░█▀▀░▀▄▀░▀▀█                     ║
 * ║   ░▀▀▀░░▀░░▀▀▀░▀▀▀░▀░▀   ░▀▀░░▀▀▀░░▀░░▀▀▀                     ║
 * ║                                                                  ║
 * ║           © 2026 Stela Devs — All Rights Reserved               ║
 * ║                                                                  ║
 * ║   discord  ──  https://discord.gg/steladev                      ║
 * ║   youtube  ──  https://youtube.com/@StelaDevs                   ║
 * ║   github   ──  https://github.com/RayExo                        ║
 * ║                                                                  ║
 * ╚══════════════════════════════════════════════════════════════════╝
 */

import NextAuth, { DefaultSession } from "next-auth";

declare module "next-auth" {
  interface Session {
    accessToken?: string;
    user: {
      id: string;
    } & DefaultSession["user"];
  }
}
