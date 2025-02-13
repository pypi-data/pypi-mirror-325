import { i as ue, a as W, r as fe, g as de, w as O, b as me } from "./Index-CwTDNjHt.js";
const E = window.ms_globals.React, Z = window.ms_globals.React.useMemo, le = window.ms_globals.React.forwardRef, ie = window.ms_globals.React.useRef, ce = window.ms_globals.React.useState, ae = window.ms_globals.React.useEffect, F = window.ms_globals.ReactDOM.createPortal, pe = window.ms_globals.internalContext.useContextPropsContext, P = window.ms_globals.internalContext.ContextPropsProvider, _e = window.ms_globals.antd.Steps, he = window.ms_globals.createItemsContext.createItemsContext;
var ge = /\s/;
function be(e) {
  for (var t = e.length; t-- && ge.test(e.charAt(t)); )
    ;
  return t;
}
var we = /^\s+/;
function xe(e) {
  return e && e.slice(0, be(e) + 1).replace(we, "");
}
var B = NaN, ye = /^[-+]0x[0-9a-f]+$/i, Ce = /^0b[01]+$/i, Ee = /^0o[0-7]+$/i, ve = parseInt;
function H(e) {
  if (typeof e == "number")
    return e;
  if (ue(e))
    return B;
  if (W(e)) {
    var t = typeof e.valueOf == "function" ? e.valueOf() : e;
    e = W(t) ? t + "" : t;
  }
  if (typeof e != "string")
    return e === 0 ? e : +e;
  e = xe(e);
  var o = Ce.test(e);
  return o || Ee.test(e) ? ve(e.slice(2), o ? 2 : 8) : ye.test(e) ? B : +e;
}
var L = function() {
  return fe.Date.now();
}, Ie = "Expected a function", Se = Math.max, Re = Math.min;
function Oe(e, t, o) {
  var l, s, n, r, i, a, b = 0, h = !1, c = !1, g = !0;
  if (typeof e != "function")
    throw new TypeError(Ie);
  t = H(t) || 0, W(o) && (h = !!o.leading, c = "maxWait" in o, n = c ? Se(H(o.maxWait) || 0, t) : n, g = "trailing" in o ? !!o.trailing : g);
  function f(p) {
    var C = l, R = s;
    return l = s = void 0, b = p, r = e.apply(R, C), r;
  }
  function w(p) {
    return b = p, i = setTimeout(_, t), h ? f(p) : r;
  }
  function d(p) {
    var C = p - a, R = p - b, U = t - C;
    return c ? Re(U, n - R) : U;
  }
  function m(p) {
    var C = p - a, R = p - b;
    return a === void 0 || C >= t || C < 0 || c && R >= n;
  }
  function _() {
    var p = L();
    if (m(p))
      return y(p);
    i = setTimeout(_, d(p));
  }
  function y(p) {
    return i = void 0, g && l ? f(p) : (l = s = void 0, r);
  }
  function v() {
    i !== void 0 && clearTimeout(i), b = 0, l = a = s = i = void 0;
  }
  function u() {
    return i === void 0 ? r : y(L());
  }
  function I() {
    var p = L(), C = m(p);
    if (l = arguments, s = this, a = p, C) {
      if (i === void 0)
        return w(a);
      if (c)
        return clearTimeout(i), i = setTimeout(_, t), f(a);
    }
    return i === void 0 && (i = setTimeout(_, t)), r;
  }
  return I.cancel = v, I.flush = u, I;
}
var $ = {
  exports: {}
}, j = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var ke = E, Te = Symbol.for("react.element"), Pe = Symbol.for("react.fragment"), je = Object.prototype.hasOwnProperty, Le = ke.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Ne = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function ee(e, t, o) {
  var l, s = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), t.key !== void 0 && (n = "" + t.key), t.ref !== void 0 && (r = t.ref);
  for (l in t) je.call(t, l) && !Ne.hasOwnProperty(l) && (s[l] = t[l]);
  if (e && e.defaultProps) for (l in t = e.defaultProps, t) s[l] === void 0 && (s[l] = t[l]);
  return {
    $$typeof: Te,
    type: e,
    key: n,
    ref: r,
    props: s,
    _owner: Le.current
  };
}
j.Fragment = Pe;
j.jsx = ee;
j.jsxs = ee;
$.exports = j;
var x = $.exports;
const {
  SvelteComponent: Fe,
  assign: z,
  binding_callbacks: G,
  check_outros: We,
  children: te,
  claim_element: ne,
  claim_space: Ae,
  component_subscribe: q,
  compute_slots: De,
  create_slot: Me,
  detach: S,
  element: re,
  empty: V,
  exclude_internal_props: J,
  get_all_dirty_from_scope: Ue,
  get_slot_changes: Be,
  group_outros: He,
  init: ze,
  insert_hydration: k,
  safe_not_equal: Ge,
  set_custom_element_data: se,
  space: qe,
  transition_in: T,
  transition_out: A,
  update_slot_base: Ve
} = window.__gradio__svelte__internal, {
  beforeUpdate: Je,
  getContext: Xe,
  onDestroy: Ye,
  setContext: Ke
} = window.__gradio__svelte__internal;
function X(e) {
  let t, o;
  const l = (
    /*#slots*/
    e[7].default
  ), s = Me(
    l,
    e,
    /*$$scope*/
    e[6],
    null
  );
  return {
    c() {
      t = re("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      t = ne(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = te(t);
      s && s.l(r), r.forEach(S), this.h();
    },
    h() {
      se(t, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      k(n, t, r), s && s.m(t, null), e[9](t), o = !0;
    },
    p(n, r) {
      s && s.p && (!o || r & /*$$scope*/
      64) && Ve(
        s,
        l,
        n,
        /*$$scope*/
        n[6],
        o ? Be(
          l,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Ue(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (T(s, n), o = !0);
    },
    o(n) {
      A(s, n), o = !1;
    },
    d(n) {
      n && S(t), s && s.d(n), e[9](null);
    }
  };
}
function Qe(e) {
  let t, o, l, s, n = (
    /*$$slots*/
    e[4].default && X(e)
  );
  return {
    c() {
      t = re("react-portal-target"), o = qe(), n && n.c(), l = V(), this.h();
    },
    l(r) {
      t = ne(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), te(t).forEach(S), o = Ae(r), n && n.l(r), l = V(), this.h();
    },
    h() {
      se(t, "class", "svelte-1rt0kpf");
    },
    m(r, i) {
      k(r, t, i), e[8](t), k(r, o, i), n && n.m(r, i), k(r, l, i), s = !0;
    },
    p(r, [i]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, i), i & /*$$slots*/
      16 && T(n, 1)) : (n = X(r), n.c(), T(n, 1), n.m(l.parentNode, l)) : n && (He(), A(n, 1, 1, () => {
        n = null;
      }), We());
    },
    i(r) {
      s || (T(n), s = !0);
    },
    o(r) {
      A(n), s = !1;
    },
    d(r) {
      r && (S(t), S(o), S(l)), e[8](null), n && n.d(r);
    }
  };
}
function Y(e) {
  const {
    svelteInit: t,
    ...o
  } = e;
  return o;
}
function Ze(e, t, o) {
  let l, s, {
    $$slots: n = {},
    $$scope: r
  } = t;
  const i = De(n);
  let {
    svelteInit: a
  } = t;
  const b = O(Y(t)), h = O();
  q(e, h, (u) => o(0, l = u));
  const c = O();
  q(e, c, (u) => o(1, s = u));
  const g = [], f = Xe("$$ms-gr-react-wrapper"), {
    slotKey: w,
    slotIndex: d,
    subSlotIndex: m
  } = de() || {}, _ = a({
    parent: f,
    props: b,
    target: h,
    slot: c,
    slotKey: w,
    slotIndex: d,
    subSlotIndex: m,
    onDestroy(u) {
      g.push(u);
    }
  });
  Ke("$$ms-gr-react-wrapper", _), Je(() => {
    b.set(Y(t));
  }), Ye(() => {
    g.forEach((u) => u());
  });
  function y(u) {
    G[u ? "unshift" : "push"](() => {
      l = u, h.set(l);
    });
  }
  function v(u) {
    G[u ? "unshift" : "push"](() => {
      s = u, c.set(s);
    });
  }
  return e.$$set = (u) => {
    o(17, t = z(z({}, t), J(u))), "svelteInit" in u && o(5, a = u.svelteInit), "$$scope" in u && o(6, r = u.$$scope);
  }, t = J(t), [l, s, h, c, i, a, r, n, y, v];
}
class $e extends Fe {
  constructor(t) {
    super(), ze(this, t, Ze, Qe, Ge, {
      svelteInit: 5
    });
  }
}
const K = window.ms_globals.rerender, N = window.ms_globals.tree;
function et(e, t = {}) {
  function o(l) {
    const s = O(), n = new $e({
      ...l,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const i = {
            key: window.ms_globals.autokey,
            svelteInstance: s,
            reactComponent: e,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: t.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, a = r.parent ?? N;
          return a.nodes = [...a.nodes, i], K({
            createPortal: F,
            node: N
          }), r.onDestroy(() => {
            a.nodes = a.nodes.filter((b) => b.svelteInstance !== s), K({
              createPortal: F,
              node: N
            });
          }), i;
        },
        ...l.props
      }
    });
    return s.set(n), n;
  }
  return new Promise((l) => {
    window.ms_globals.initializePromise.then(() => {
      l(o);
    });
  });
}
function tt(e) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(e.trim());
}
function nt(e, t = !1) {
  try {
    if (me(e))
      return e;
    if (t && !tt(e))
      return;
    if (typeof e == "string") {
      let o = e.trim();
      return o.startsWith(";") && (o = o.slice(1)), o.endsWith(";") && (o = o.slice(0, -1)), new Function(`return (...args) => (${o})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function rt(e, t) {
  return Z(() => nt(e, t), [e, t]);
}
const st = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function ot(e) {
  return e ? Object.keys(e).reduce((t, o) => {
    const l = e[o];
    return t[o] = lt(o, l), t;
  }, {}) : {};
}
function lt(e, t) {
  return typeof t == "number" && !st.includes(e) ? t + "px" : t;
}
function D(e) {
  const t = [], o = e.cloneNode(!1);
  if (e._reactElement) {
    const s = E.Children.toArray(e._reactElement.props.children).map((n) => {
      if (E.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: i
        } = D(n.props.el);
        return E.cloneElement(n, {
          ...n.props,
          el: i,
          children: [...E.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = e._reactElement.props.children, t.push(F(E.cloneElement(e._reactElement, {
      ...e._reactElement.props,
      children: s
    }), o)), {
      clonedElement: o,
      portals: t
    };
  }
  Object.keys(e.getEventListeners()).forEach((s) => {
    e.getEventListeners(s).forEach(({
      listener: r,
      type: i,
      useCapture: a
    }) => {
      o.addEventListener(i, r, a);
    });
  });
  const l = Array.from(e.childNodes);
  for (let s = 0; s < l.length; s++) {
    const n = l[s];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: i
      } = D(n);
      t.push(...i), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: t
  };
}
function it(e, t) {
  e && (typeof e == "function" ? e(t) : e.current = t);
}
const M = le(({
  slot: e,
  clone: t,
  className: o,
  style: l,
  observeAttributes: s
}, n) => {
  const r = ie(), [i, a] = ce([]), {
    forceClone: b
  } = pe(), h = b ? !0 : t;
  return ae(() => {
    var w;
    if (!r.current || !e)
      return;
    let c = e;
    function g() {
      let d = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (d = c.children[0], d.tagName.toLowerCase() === "react-portal-target" && d.children[0] && (d = d.children[0])), it(n, d), o && d.classList.add(...o.split(" ")), l) {
        const m = ot(l);
        Object.keys(m).forEach((_) => {
          d.style[_] = m[_];
        });
      }
    }
    let f = null;
    if (h && window.MutationObserver) {
      let d = function() {
        var v, u, I;
        (v = r.current) != null && v.contains(c) && ((u = r.current) == null || u.removeChild(c));
        const {
          portals: _,
          clonedElement: y
        } = D(e);
        c = y, a(_), c.style.display = "contents", g(), (I = r.current) == null || I.appendChild(c);
      };
      d();
      const m = Oe(() => {
        d(), f == null || f.disconnect(), f == null || f.observe(e, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      f = new window.MutationObserver(m), f.observe(e, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", g(), (w = r.current) == null || w.appendChild(c);
    return () => {
      var d, m;
      c.style.display = "", (d = r.current) != null && d.contains(c) && ((m = r.current) == null || m.removeChild(c)), f == null || f.disconnect();
    };
  }, [e, h, o, l, n, s]), E.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...i);
});
function oe(e, t, o) {
  const l = e.filter(Boolean);
  if (l.length !== 0)
    return l.map((s, n) => {
      var b;
      if (typeof s != "object")
        return s;
      const r = {
        ...s.props,
        key: ((b = s.props) == null ? void 0 : b.key) ?? (o ? `${o}-${n}` : `${n}`)
      };
      let i = r;
      Object.keys(s.slots).forEach((h) => {
        if (!s.slots[h] || !(s.slots[h] instanceof Element) && !s.slots[h].el)
          return;
        const c = h.split(".");
        c.forEach((_, y) => {
          i[_] || (i[_] = {}), y !== c.length - 1 && (i = r[_]);
        });
        const g = s.slots[h];
        let f, w, d = !1, m = t == null ? void 0 : t.forceClone;
        g instanceof Element ? f = g : (f = g.el, w = g.callback, d = g.clone ?? d, m = g.forceClone ?? m), m = m ?? !!w, i[c[c.length - 1]] = f ? w ? (..._) => (w(c[c.length - 1], _), /* @__PURE__ */ x.jsx(P, {
          params: _,
          forceClone: m,
          children: /* @__PURE__ */ x.jsx(M, {
            slot: f,
            clone: d
          })
        })) : /* @__PURE__ */ x.jsx(P, {
          forceClone: m,
          children: /* @__PURE__ */ x.jsx(M, {
            slot: f,
            clone: d
          })
        }) : i[c[c.length - 1]], i = r;
      });
      const a = "children";
      return s[a] && (r[a] = oe(s[a], t, `${n}`)), r;
    });
}
function Q(e, t) {
  return e ? /* @__PURE__ */ x.jsx(M, {
    slot: e,
    clone: t == null ? void 0 : t.clone
  }) : null;
}
function ct({
  key: e,
  slots: t,
  targets: o
}, l) {
  return t[e] ? (...s) => o ? o.map((n, r) => /* @__PURE__ */ x.jsx(P, {
    params: s,
    forceClone: (l == null ? void 0 : l.forceClone) ?? !0,
    children: Q(n, {
      clone: !0,
      ...l
    })
  }, r)) : /* @__PURE__ */ x.jsx(P, {
    params: s,
    forceClone: (l == null ? void 0 : l.forceClone) ?? !0,
    children: Q(t[e], {
      clone: !0,
      ...l
    })
  }) : void 0;
}
const {
  withItemsContextProvider: at,
  useItems: ut,
  ItemHandler: dt
} = he("antd-steps-items"), mt = et(at(["items", "default"], ({
  slots: e,
  items: t,
  setSlotParams: o,
  children: l,
  progressDot: s,
  ...n
}) => {
  const {
    items: r
  } = ut(), i = r.items.length > 0 ? r.items : r.default, a = rt(s);
  return /* @__PURE__ */ x.jsxs(x.Fragment, {
    children: [/* @__PURE__ */ x.jsx("div", {
      style: {
        display: "none"
      },
      children: l
    }), /* @__PURE__ */ x.jsx(_e, {
      ...n,
      items: Z(() => t || oe(i), [t, i]),
      progressDot: e.progressDot ? ct({
        slots: e,
        setSlotParams: o,
        key: "progressDot"
      }, {
        clone: !0
      }) : a || s
    })]
  });
}));
export {
  mt as Steps,
  mt as default
};
