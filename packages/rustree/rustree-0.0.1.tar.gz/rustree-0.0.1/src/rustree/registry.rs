// Copyright 2024-2025 Xuehai Pan. All Rights Reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
// =============================================================================

use once_cell::sync::OnceCell;
use pyo3::prelude::*;
use pyo3::types::*;
use std::collections::{HashMap, HashSet};

#[pyclass(eq, eq_int, module = "rustree")]
#[derive(PartialEq)]
pub enum PyTreeKind {
    CUSTOM = 0,
    LEAF,
    NONE,
    TUPLE,
    LIST,
    DICT,
    NAMEDTUPLE,
    ORDEREDDICT,
    DEFAULTDICT,
    DEQUE,
    STRUCTSEQUENCE,
}

struct PyTreeTypeRegistration {
    kind: PyTreeKind,
    type_: Py<PyType>,
    flatten_func: Py<PyFunction>,
    unflatten_func: Py<PyFunction>,
    path_entry_type: Py<PyType>,
}

pub struct PyTreeTypeRegistry {
    registrations: HashMap<Py<PyType>, PyTreeTypeRegistration>,
    named_registrations: HashMap<(String, Py<PyType>), PyTreeTypeRegistration>,
}

static REGISTRY: OnceCell<PyTreeTypeRegistry> = OnceCell::new();
