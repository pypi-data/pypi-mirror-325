import { i as ue, a as B, r as fe, g as me, w as k, b as pe } from "./Index-DGngvv6F.js";
const y = window.ms_globals.React, ie = window.ms_globals.React.forwardRef, ce = window.ms_globals.React.useRef, de = window.ms_globals.React.useState, ae = window.ms_globals.React.useEffect, F = window.ms_globals.ReactDOM.createPortal, he = window.ms_globals.internalContext.useContextPropsContext, T = window.ms_globals.internalContext.ContextPropsProvider, ee = window.ms_globals.createItemsContext.createItemsContext;
var _e = /\s/;
function we(t) {
  for (var e = t.length; e-- && _e.test(t.charAt(e)); )
    ;
  return e;
}
var ge = /^\s+/;
function be(t) {
  return t && t.slice(0, we(t) + 1).replace(ge, "");
}
var G = NaN, ve = /^[-+]0x[0-9a-f]+$/i, xe = /^0b[01]+$/i, Ie = /^0o[0-7]+$/i, Ce = parseInt;
function q(t) {
  if (typeof t == "number")
    return t;
  if (ue(t))
    return G;
  if (B(t)) {
    var e = typeof t.valueOf == "function" ? t.valueOf() : t;
    t = B(e) ? e + "" : e;
  }
  if (typeof t != "string")
    return t === 0 ? t : +t;
  t = be(t);
  var l = xe.test(t);
  return l || Ie.test(t) ? Ce(t.slice(2), l ? 2 : 8) : ve.test(t) ? G : +t;
}
var N = function() {
  return fe.Date.now();
}, ye = "Expected a function", Ee = Math.max, Re = Math.min;
function Se(t, e, l) {
  var s, o, n, r, i, d, g = 0, h = !1, c = !1, _ = !0;
  if (typeof t != "function")
    throw new TypeError(ye);
  e = q(e) || 0, B(l) && (h = !!l.leading, c = "maxWait" in l, n = c ? Ee(q(l.maxWait) || 0, e) : n, _ = "trailing" in l ? !!l.trailing : _);
  function a(w) {
    var I = s, S = o;
    return s = o = void 0, g = w, r = t.apply(S, I), r;
  }
  function b(w) {
    return g = w, i = setTimeout(p, e), h ? a(w) : r;
  }
  function u(w) {
    var I = w - d, S = w - g, z = e - I;
    return c ? Re(z, n - S) : z;
  }
  function m(w) {
    var I = w - d, S = w - g;
    return d === void 0 || I >= e || I < 0 || c && S >= n;
  }
  function p() {
    var w = N();
    if (m(w))
      return v(w);
    i = setTimeout(p, u(w));
  }
  function v(w) {
    return i = void 0, _ && s ? a(w) : (s = o = void 0, r);
  }
  function x() {
    i !== void 0 && clearTimeout(i), g = 0, s = d = o = i = void 0;
  }
  function f() {
    return i === void 0 ? r : v(N());
  }
  function E() {
    var w = N(), I = m(w);
    if (s = arguments, o = this, d = w, I) {
      if (i === void 0)
        return b(d);
      if (c)
        return clearTimeout(i), i = setTimeout(p, e), a(d);
    }
    return i === void 0 && (i = setTimeout(p, e)), r;
  }
  return E.cancel = x, E.flush = f, E;
}
var te = {
  exports: {}
}, L = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var ke = y, Oe = Symbol.for("react.element"), Pe = Symbol.for("react.fragment"), Te = Object.prototype.hasOwnProperty, je = ke.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Le = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function ne(t, e, l) {
  var s, o = {}, n = null, r = null;
  l !== void 0 && (n = "" + l), e.key !== void 0 && (n = "" + e.key), e.ref !== void 0 && (r = e.ref);
  for (s in e) Te.call(e, s) && !Le.hasOwnProperty(s) && (o[s] = e[s]);
  if (t && t.defaultProps) for (s in e = t.defaultProps, e) o[s] === void 0 && (o[s] = e[s]);
  return {
    $$typeof: Oe,
    type: t,
    key: n,
    ref: r,
    props: o,
    _owner: je.current
  };
}
L.Fragment = Pe;
L.jsx = ne;
L.jsxs = ne;
te.exports = L;
var C = te.exports;
const {
  SvelteComponent: Ne,
  assign: V,
  binding_callbacks: J,
  check_outros: We,
  children: re,
  claim_element: oe,
  claim_space: Ae,
  component_subscribe: X,
  compute_slots: Fe,
  create_slot: Be,
  detach: R,
  element: le,
  empty: Y,
  exclude_internal_props: K,
  get_all_dirty_from_scope: Me,
  get_slot_changes: De,
  group_outros: He,
  init: Ue,
  insert_hydration: O,
  safe_not_equal: ze,
  set_custom_element_data: se,
  space: Ge,
  transition_in: P,
  transition_out: M,
  update_slot_base: qe
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ve,
  getContext: Je,
  onDestroy: Xe,
  setContext: Ye
} = window.__gradio__svelte__internal;
function Q(t) {
  let e, l;
  const s = (
    /*#slots*/
    t[7].default
  ), o = Be(
    s,
    t,
    /*$$scope*/
    t[6],
    null
  );
  return {
    c() {
      e = le("svelte-slot"), o && o.c(), this.h();
    },
    l(n) {
      e = oe(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = re(e);
      o && o.l(r), r.forEach(R), this.h();
    },
    h() {
      se(e, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      O(n, e, r), o && o.m(e, null), t[9](e), l = !0;
    },
    p(n, r) {
      o && o.p && (!l || r & /*$$scope*/
      64) && qe(
        o,
        s,
        n,
        /*$$scope*/
        n[6],
        l ? De(
          s,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Me(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      l || (P(o, n), l = !0);
    },
    o(n) {
      M(o, n), l = !1;
    },
    d(n) {
      n && R(e), o && o.d(n), t[9](null);
    }
  };
}
function Ke(t) {
  let e, l, s, o, n = (
    /*$$slots*/
    t[4].default && Q(t)
  );
  return {
    c() {
      e = le("react-portal-target"), l = Ge(), n && n.c(), s = Y(), this.h();
    },
    l(r) {
      e = oe(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), re(e).forEach(R), l = Ae(r), n && n.l(r), s = Y(), this.h();
    },
    h() {
      se(e, "class", "svelte-1rt0kpf");
    },
    m(r, i) {
      O(r, e, i), t[8](e), O(r, l, i), n && n.m(r, i), O(r, s, i), o = !0;
    },
    p(r, [i]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, i), i & /*$$slots*/
      16 && P(n, 1)) : (n = Q(r), n.c(), P(n, 1), n.m(s.parentNode, s)) : n && (He(), M(n, 1, 1, () => {
        n = null;
      }), We());
    },
    i(r) {
      o || (P(n), o = !0);
    },
    o(r) {
      M(n), o = !1;
    },
    d(r) {
      r && (R(e), R(l), R(s)), t[8](null), n && n.d(r);
    }
  };
}
function Z(t) {
  const {
    svelteInit: e,
    ...l
  } = t;
  return l;
}
function Qe(t, e, l) {
  let s, o, {
    $$slots: n = {},
    $$scope: r
  } = e;
  const i = Fe(n);
  let {
    svelteInit: d
  } = e;
  const g = k(Z(e)), h = k();
  X(t, h, (f) => l(0, s = f));
  const c = k();
  X(t, c, (f) => l(1, o = f));
  const _ = [], a = Je("$$ms-gr-react-wrapper"), {
    slotKey: b,
    slotIndex: u,
    subSlotIndex: m
  } = me() || {}, p = d({
    parent: a,
    props: g,
    target: h,
    slot: c,
    slotKey: b,
    slotIndex: u,
    subSlotIndex: m,
    onDestroy(f) {
      _.push(f);
    }
  });
  Ye("$$ms-gr-react-wrapper", p), Ve(() => {
    g.set(Z(e));
  }), Xe(() => {
    _.forEach((f) => f());
  });
  function v(f) {
    J[f ? "unshift" : "push"](() => {
      s = f, h.set(s);
    });
  }
  function x(f) {
    J[f ? "unshift" : "push"](() => {
      o = f, c.set(o);
    });
  }
  return t.$$set = (f) => {
    l(17, e = V(V({}, e), K(f))), "svelteInit" in f && l(5, d = f.svelteInit), "$$scope" in f && l(6, r = f.$$scope);
  }, e = K(e), [s, o, h, c, i, d, r, n, v, x];
}
class Ze extends Ne {
  constructor(e) {
    super(), Ue(this, e, Qe, Ke, ze, {
      svelteInit: 5
    });
  }
}
const $ = window.ms_globals.rerender, W = window.ms_globals.tree;
function $e(t, e = {}) {
  function l(s) {
    const o = k(), n = new Ze({
      ...s,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const i = {
            key: window.ms_globals.autokey,
            svelteInstance: o,
            reactComponent: t,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: e.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, d = r.parent ?? W;
          return d.nodes = [...d.nodes, i], $({
            createPortal: F,
            node: W
          }), r.onDestroy(() => {
            d.nodes = d.nodes.filter((g) => g.svelteInstance !== o), $({
              createPortal: F,
              node: W
            });
          }), i;
        },
        ...s.props
      }
    });
    return o.set(n), n;
  }
  return new Promise((s) => {
    window.ms_globals.initializePromise.then(() => {
      s(l);
    });
  });
}
function et(t) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(t.trim());
}
function tt(t, e = !1) {
  try {
    if (pe(t))
      return t;
    if (e && !et(t))
      return;
    if (typeof t == "string") {
      let l = t.trim();
      return l.startsWith(";") && (l = l.slice(1)), l.endsWith(";") && (l = l.slice(0, -1)), new Function(`return (...args) => (${l})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
const nt = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function rt(t) {
  return t ? Object.keys(t).reduce((e, l) => {
    const s = t[l];
    return e[l] = ot(l, s), e;
  }, {}) : {};
}
function ot(t, e) {
  return typeof e == "number" && !nt.includes(t) ? e + "px" : e;
}
function D(t) {
  const e = [], l = t.cloneNode(!1);
  if (t._reactElement) {
    const o = y.Children.toArray(t._reactElement.props.children).map((n) => {
      if (y.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: i
        } = D(n.props.el);
        return y.cloneElement(n, {
          ...n.props,
          el: i,
          children: [...y.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return o.originalChildren = t._reactElement.props.children, e.push(F(y.cloneElement(t._reactElement, {
      ...t._reactElement.props,
      children: o
    }), l)), {
      clonedElement: l,
      portals: e
    };
  }
  Object.keys(t.getEventListeners()).forEach((o) => {
    t.getEventListeners(o).forEach(({
      listener: r,
      type: i,
      useCapture: d
    }) => {
      l.addEventListener(i, r, d);
    });
  });
  const s = Array.from(t.childNodes);
  for (let o = 0; o < s.length; o++) {
    const n = s[o];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: i
      } = D(n);
      e.push(...i), l.appendChild(r);
    } else n.nodeType === 3 && l.appendChild(n.cloneNode());
  }
  return {
    clonedElement: l,
    portals: e
  };
}
function lt(t, e) {
  t && (typeof t == "function" ? t(e) : t.current = e);
}
const H = ie(({
  slot: t,
  clone: e,
  className: l,
  style: s,
  observeAttributes: o
}, n) => {
  const r = ce(), [i, d] = de([]), {
    forceClone: g
  } = he(), h = g ? !0 : e;
  return ae(() => {
    var b;
    if (!r.current || !t)
      return;
    let c = t;
    function _() {
      let u = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (u = c.children[0], u.tagName.toLowerCase() === "react-portal-target" && u.children[0] && (u = u.children[0])), lt(n, u), l && u.classList.add(...l.split(" ")), s) {
        const m = rt(s);
        Object.keys(m).forEach((p) => {
          u.style[p] = m[p];
        });
      }
    }
    let a = null;
    if (h && window.MutationObserver) {
      let u = function() {
        var x, f, E;
        (x = r.current) != null && x.contains(c) && ((f = r.current) == null || f.removeChild(c));
        const {
          portals: p,
          clonedElement: v
        } = D(t);
        c = v, d(p), c.style.display = "contents", _(), (E = r.current) == null || E.appendChild(c);
      };
      u();
      const m = Se(() => {
        u(), a == null || a.disconnect(), a == null || a.observe(t, {
          childList: !0,
          subtree: !0,
          attributes: o
        });
      }, 50);
      a = new window.MutationObserver(m), a.observe(t, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", _(), (b = r.current) == null || b.appendChild(c);
    return () => {
      var u, m;
      c.style.display = "", (u = r.current) != null && u.contains(c) && ((m = r.current) == null || m.removeChild(c)), a == null || a.disconnect();
    };
  }, [t, h, l, s, n, o]), y.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...i);
});
function U(t, e, l) {
  const s = t.filter(Boolean);
  if (s.length !== 0)
    return s.map((o, n) => {
      var g;
      if (typeof o != "object")
        return e != null && e.fallback ? e.fallback(o) : o;
      const r = {
        ...o.props,
        key: ((g = o.props) == null ? void 0 : g.key) ?? (l ? `${l}-${n}` : `${n}`)
      };
      let i = r;
      Object.keys(o.slots).forEach((h) => {
        if (!o.slots[h] || !(o.slots[h] instanceof Element) && !o.slots[h].el)
          return;
        const c = h.split(".");
        c.forEach((p, v) => {
          i[p] || (i[p] = {}), v !== c.length - 1 && (i = r[p]);
        });
        const _ = o.slots[h];
        let a, b, u = (e == null ? void 0 : e.clone) ?? !1, m = e == null ? void 0 : e.forceClone;
        _ instanceof Element ? a = _ : (a = _.el, b = _.callback, u = _.clone ?? u, m = _.forceClone ?? m), m = m ?? !!b, i[c[c.length - 1]] = a ? b ? (...p) => (b(c[c.length - 1], p), /* @__PURE__ */ C.jsx(T, {
          params: p,
          forceClone: m,
          children: /* @__PURE__ */ C.jsx(H, {
            slot: a,
            clone: u
          })
        })) : /* @__PURE__ */ C.jsx(T, {
          forceClone: m,
          children: /* @__PURE__ */ C.jsx(H, {
            slot: a,
            clone: u
          })
        }) : i[c[c.length - 1]], i = r;
      });
      const d = (e == null ? void 0 : e.children) || "children";
      return o[d] ? r[d] = U(o[d], e, `${n}`) : e != null && e.children && (r[d] = void 0, Reflect.deleteProperty(r, d)), r;
    });
}
function j(t, e) {
  return t ? /* @__PURE__ */ C.jsx(H, {
    slot: t,
    clone: e == null ? void 0 : e.clone
  }) : null;
}
function A({
  key: t,
  slots: e,
  targets: l
}, s) {
  return e[t] ? (...o) => l ? l.map((n, r) => /* @__PURE__ */ C.jsx(T, {
    params: o,
    forceClone: (s == null ? void 0 : s.forceClone) ?? !0,
    children: j(n, {
      clone: !0,
      ...s
    })
  }, r)) : /* @__PURE__ */ C.jsx(T, {
    params: o,
    forceClone: (s == null ? void 0 : s.forceClone) ?? !0,
    children: j(e[t], {
      clone: !0,
      ...s
    })
  }) : void 0;
}
const {
  useItems: st,
  withItemsContextProvider: it,
  ItemHandler: at
} = ee("antd-menu-items"), {
  useItems: ut,
  withItemsContextProvider: ft,
  ItemHandler: ct
} = ee("antd-breadcrumb-items"), mt = $e(it(["menu.items", "dropdownProps.menu.items"], ({
  setSlotParams: t,
  itemSlots: e,
  ...l
}) => {
  const {
    items: {
      "menu.items": s,
      "dropdownProps.menu.items": o
    }
  } = st();
  return /* @__PURE__ */ C.jsx(ct, {
    ...l,
    itemProps: (n) => {
      var g, h, c, _, a, b, u, m, p, v, x;
      const r = {
        ...n.menu || {},
        items: (g = n.menu) != null && g.items || s.length > 0 ? U(s, {
          clone: !0
        }) : void 0,
        expandIcon: A({
          setSlotParams: t,
          slots: e,
          key: "menu.expandIcon"
        }, {
          clone: !0
        }) || ((h = n.menu) == null ? void 0 : h.expandIcon),
        overflowedIndicator: j(e["menu.overflowedIndicator"]) || ((c = n.menu) == null ? void 0 : c.overflowedIndicator)
      }, i = {
        ...((_ = n.dropdownProps) == null ? void 0 : _.menu) || {},
        items: (b = (a = n.dropdownProps) == null ? void 0 : a.menu) != null && b.items || o.length > 0 ? U(o, {
          clone: !0
        }) : void 0,
        expandIcon: A({
          setSlotParams: t,
          slots: e,
          key: "dropdownProps.menu.expandIcon"
        }, {
          clone: !0
        }) || ((m = (u = n.dropdownProps) == null ? void 0 : u.menu) == null ? void 0 : m.expandIcon),
        overflowedIndicator: j(e["dropdownProps.menu.overflowedIndicator"]) || ((v = (p = n.dropdownProps) == null ? void 0 : p.menu) == null ? void 0 : v.overflowedIndicator)
      }, d = {
        ...n.dropdownProps || {},
        dropdownRender: e["dropdownProps.dropdownRender"] ? A({
          setSlotParams: t,
          slots: e,
          key: "dropdownProps.dropdownRender"
        }, {
          clone: !0
        }) : tt((x = n.dropdownProps) == null ? void 0 : x.dropdownRender),
        menu: Object.values(i).filter(Boolean).length > 0 ? i : void 0
      };
      return {
        ...n,
        menu: Object.values(r).filter(Boolean).length > 0 ? r : void 0,
        dropdownProps: Object.values(d).filter(Boolean).length > 0 ? d : void 0
      };
    }
  });
}));
export {
  mt as BreadcrumbItem,
  mt as default
};
