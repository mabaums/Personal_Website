/**
 * Simple Inventory API
 * This is a simple API
 *
 * OpenAPI spec version: 1.1.0
 * Contact: you@your-company.com
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

export interface Team { 
    rk: number;
    squad: string;
    MP?: number;
    W: number;
    D: number;
    L: number;
    GF: number;
    GA: number;
    GD: string;
    x_ga: number;
    x_g: number;
    x_gd: string;
    x_gd90: string;
    attendance: number;
    top_scorer?: string;
    goalkeepr?: string;
    pts: number;
    notes: string;
}